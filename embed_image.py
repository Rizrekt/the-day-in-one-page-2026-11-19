"""Build helper: embed ../entry-candidate-PJ3-v8c-POSTER.png into main.py as base64."""

import base64
import pathlib

REPO_DIR = pathlib.Path(__file__).resolve().parent
SOURCE_PNG = REPO_DIR.parent / "entry-candidate-PJ3-v8c-POSTER.png"
TARGET = REPO_DIR / "main.py"
PLACEHOLDER = "__PAYLOAD__"


def main():
    source_bytes = SOURCE_PNG.read_bytes()
    encoded = base64.b64encode(source_bytes).decode("ascii")

    lines = TARGET.read_text(encoding="utf-8").splitlines(keepends=True)
    for index, line in enumerate(lines):
        if PLACEHOLDER in line:
            lines[index] = f'PNG_B64 = "{encoded}"\n'
            break
    else:
        raise SystemExit(f"no line containing {PLACEHOLDER!r} found in {TARGET}")
    TARGET.write_text("".join(lines), encoding="utf-8")

    payload_lines = [
        line
        for line in TARGET.read_text(encoding="utf-8").splitlines()
        if line.startswith("PNG_B64 = ")
    ]
    if len(payload_lines) != 1:
        raise SystemExit("expected exactly one PNG_B64 line in main.py after embedding")
    embedded = payload_lines[0][len('PNG_B64 = "') : -1]
    verified = base64.b64decode(embedded) == source_bytes

    print(f"embedded {len(encoded)} base64 chars")
    print(f"source: {SOURCE_PNG}")
    print(f"target: {TARGET}")
    print(f"verification: {'PASS' if verified else 'FAIL'}")
    if not verified:
        raise SystemExit("embedded payload does not match the source PNG bytes")


if __name__ == "__main__":
    main()
