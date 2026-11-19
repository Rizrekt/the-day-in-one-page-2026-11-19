"""Build helper: embed ../entry-candidate-v2.png into main.py as base64.

The payload written into the target is read back and verified against the
source bytes before the helper reports success.
"""

import argparse
import ast
import base64
import hashlib
import pathlib

REPO_DIR = pathlib.Path(__file__).resolve().parent
DEFAULT_SOURCE = REPO_DIR.parent / "entry-candidate-v2.png"
DEFAULT_TARGET = REPO_DIR / "main.py"

PREFIX = "PNG_B64 ="


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--source",
        type=pathlib.Path,
        default=DEFAULT_SOURCE,
        help="PNG to embed (default: %(default)s)",
    )
    parser.add_argument(
        "--target",
        type=pathlib.Path,
        default=DEFAULT_TARGET,
        help="file holding the PNG_B64 line (default: %(default)s)",
    )
    return parser.parse_args(argv)


def encode(raw):
    return base64.b64encode(raw).decode("ascii")


def replace_line(text, payload):
    lines = text.splitlines(keepends=True)
    hits = [i for i, line in enumerate(lines) if line.lstrip().startswith(PREFIX)]
    if not hits:
        raise SystemExit(f"error: no line beginning with {PREFIX!r} in target")
    if len(hits) > 1:
        raise SystemExit(
            f"error: {PREFIX!r} line appears {len(hits)} times, expected exactly once"
        )
    index = hits[0]
    terminator = "\n" if lines[index].endswith("\n") else ""
    lines[index] = f'{PREFIX} "{payload}"{terminator}'
    return "".join(lines)


def extract(text):
    for line in text.splitlines():
        if line.lstrip().startswith(PREFIX):
            _, _, literal = line.lstrip().partition("=")
            value = ast.literal_eval(literal.strip())
            if not isinstance(value, str):
                raise SystemExit("error: embedded PNG_B64 value is not a string")
            return value
    raise SystemExit("error: could not find the embedded PNG_B64 value")


def verify(target, expected):
    payload = extract(target.read_text(encoding="utf-8"))
    try:
        decoded = base64.b64decode(payload, validate=True)
    except ValueError as exc:
        raise SystemExit(f"error: embedded payload does not decode: {exc}")
    if decoded != expected:
        raise SystemExit("error: verification failed, embedded bytes differ from source")


def main(argv=None):
    args = parse_args(argv)
    source = args.source.resolve()
    target = args.target.resolve()

    raw = source.read_bytes()
    payload = encode(raw)

    text = target.read_text(encoding="utf-8")
    target.write_text(replace_line(text, payload), encoding="utf-8")
    verify(target, raw)

    print(f"embedded: {len(payload)} base64 characters")
    print(f"source bytes: {len(raw)}")
    print(f"source sha256: {hashlib.sha256(raw).hexdigest()}")
    print("verified: decoded payload matches source byte for byte")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
