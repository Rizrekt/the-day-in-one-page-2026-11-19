"""One-shot helper: collapse a wrapped PNG_B64 payload in main.py onto a single line."""

import ast
import base64
import pathlib

TARGET = pathlib.Path(__file__).resolve().parent / "main.py"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def find_payload_assignment(tree: ast.Module) -> ast.Assign:
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and node.targets[0].id == "PNG_B64"
        ):
            return node
    raise SystemExit(f"PNG_B64 assignment not found in {TARGET}")


def main() -> None:
    text = TARGET.read_text(encoding="utf-8")
    node = find_payload_assignment(ast.parse(text))

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
