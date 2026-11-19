"""Build helper: embed ../entry-candidate-PJ3-v2.png into main.py as base64."""

import ast
import base64
import pathlib

REPO_DIR = pathlib.Path(__file__).resolve().parent
SOURCE_PNG = REPO_DIR.parent / "entry-candidate-PJ3-v2.png"
TARGET = REPO_DIR / "main.py"
PLACEHOLDER = "__PAYLOAD__"


def embedded_payload() -> str:
    for node in ast.parse(TARGET.read_text(encoding="utf-8")).body:
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and node.targets[0].id == "PNG_B64"
        ):
            return ast.literal_eval(node.value)
    raise SystemExit(f"PNG_B64 assignment not found in {TARGET}")


def main() -> None:
    source_bytes = SOURCE_PNG.read_bytes()
    encoded = base64.b64encode(source_bytes).decode("ascii")

    lines = TARGET.read_text(encoding="utf-8").splitlines(keepends=True)
    hits = [index for index, line in enumerate(lines) if PLACEHOLDER in line]
    if len(hits) != 1:
        raise SystemExit(
            f"expected exactly one line containing {PLACEHOLDER!r} in {TARGET}, "
            f"found {len(hits)}"
        )
    lines[hits[0]] = f'PNG_B64 = "{encoded}"\n'
    TARGET.write_text("".join(lines), encoding="utf-8")

    payload = embedded_payload()
    verified = base64.b64decode(payload) == source_bytes
    print(f"embedded {len(payload)} base64 chars")
    print(f"source: {SOURCE_PNG}")
    print(f"target: {TARGET}")
    print(f"verification passed: {verified}")
    if not verified:
        raise SystemExit("verification failed: embedded bytes differ from source PNG")


if __name__ == "__main__":
    main()
