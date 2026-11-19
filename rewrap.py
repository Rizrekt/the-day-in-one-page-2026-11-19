"""One-shot helper: collapse a wrapped PNG_B64 payload in main.py onto one line."""

import ast
import base64
import pathlib

TARGET = pathlib.Path(__file__).resolve().parent / "main.py"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main() -> None:
    text = TARGET.read_text(encoding="utf-8")

    node = None
    for candidate in ast.parse(text).body:
        if (
            isinstance(candidate, ast.Assign)
            and len(candidate.targets) == 1
            and isinstance(candidate.targets[0], ast.Name)
            and candidate.targets[0].id == "PNG_B64"
        ):
            node = candidate
            break
    if node is None:
        raise SystemExit(f"PNG_B64 assignment not found in {TARGET}")

    payload = ast.literal_eval(node.value)
    decoded = base64.b64decode(payload)
    if not decoded.startswith(PNG_MAGIC):
        raise SystemExit("decoded PNG_B64 payload does not start with PNG magic bytes")

    lines = text.splitlines(keepends=True)
    lines[node.lineno - 1 : node.end_lineno] = [f'PNG_B64 = "{payload}"\n']
    TARGET.write_text("".join(lines), encoding="utf-8")

    print(f"rewrapped {len(payload)} base64 chars")
    print(f"decoded bytes: {len(decoded)}")


if __name__ == "__main__":
    main()
