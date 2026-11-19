"""Build helper: embed ../entry-candidate-PJ3-v2.png into main.py as base64."""

import base64
import pathlib

REPO_DIR = pathlib.Path(__file__).resolve().parent
SOURCE_PNG = REPO_DIR.parent / "entry-candidate-PJ3-v2.png"
TARGET = REPO_DIR / "main.py"
PLACEHOLDER = "__PAYLOAD__"


def main() -> None:
    source_bytes = SOURCE_PNG.read_bytes()
    encoded = base64.b64encode(source_bytes).decode("ascii")

    lines = TARGET.read_text(encoding="utf-8").splitlines(keepends=True)
    hits = [i for i, line in enumerate(lines) if PLACEHOLDER in line]
    if len(hits) != 1:
        raise SystemExit(
            f"expected exactly one line containing {PLACEHOLDER!r} in {TARGET}, "
            f"found {len(hits)}"
        )
    lines[hits[0]] = f'PNG_B64 = "{encoded}"\n'
    TARGET.write_text("".join(lines), encoding="utf-8")

    embedded = next(
        (
            line
            for line in TARGET.read_text(encoding="utf-8").splitlines()
            if line.startswith("PNG_B64 = ")
        ),
        None,
    )
    if embedded is None:
        raise SystemExit(f"no PNG_B64 assignment found in {TARGET}")
    payload = embedded.removeprefix("PNG_B64 = ").strip().strip('"')
    ok = base64.b64decode(payload) == source_bytes

    print(f"embedded {len(payload)} base64 chars")
    print(f"source: {SOURCE_PNG}")
    print(f"target: {TARGET}")
    print(f"verification passed: {ok}")
    if not ok:
        raise SystemExit("verification failed: embedded bytes differ from source PNG")


if __name__ == "__main__":
    main()
