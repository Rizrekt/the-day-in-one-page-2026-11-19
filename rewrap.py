"""One-shot helper: collapse a wrapped PNG_B64 payload in main.py to one line.

This script exists only to repair a payload that was split across several
string literals; it is not needed to run the entry. Keep it around as a
build-time utility, or drop it once the payload is a single line again.
"""

import ast
import base64
import hashlib
import pathlib
import sys

TARGET = pathlib.Path(__file__).resolve().parent / "main.py"
NAME = "PNG_B64"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def find_assignment(tree):
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == NAME:
                return node
    raise SystemExit(f"error: no assignment to {NAME} found")


def string_value(node):
    if not isinstance(node.value, ast.Constant) or not isinstance(node.value.value, str):
        raise SystemExit(f"error: {NAME} is not a plain string literal")
    return node.value.value


def decoded_payload(payload):
    try:
        raw = base64.b64decode(payload, validate=True)
    except ValueError as exc:
        raise SystemExit(f"error: {NAME} does not decode as base64: {exc}")
    if not raw.startswith(PNG_MAGIC):
        raise SystemExit(f"error: {NAME} does not decode to a PNG")
    return raw


def collapse(text, node, payload):
    lines = text.splitlines(keepends=True)
    start = node.lineno - 1
    stop = node.end_lineno
    indent = lines[start][: len(lines[start]) - len(lines[start].lstrip())]
    terminator = "\n" if lines[start].endswith("\n") else ""
    lines[start:stop] = [f'{indent}{NAME} = "{payload}"{terminator}']
    return "".join(lines)


def main():
    text = TARGET.read_text(encoding="utf-8")
    try:
        tree = ast.parse(text)
    except SyntaxError as exc:
        raise SystemExit(f"error: cannot parse {TARGET.name}: {exc}")

    node = find_assignment(tree)
    payload = string_value(node)
    raw = decoded_payload(payload)

    print(f"decoded bytes: {len(raw)}")
    print(f"decoded sha256: {hashlib.sha256(raw).hexdigest()}")

    updated = collapse(text, node, payload)
    TARGET.write_text(updated, encoding="utf-8")

    try:
        ast.parse(updated)
    except SyntaxError as exc:
        raise SystemExit(f"error: rewrapped file no longer parses: {exc}")

    print(f"rewrapped {len(payload)} base64 characters onto a single line")
    return 0


if __name__ == "__main__":
    sys.exit(main())
