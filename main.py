"""Make the AI judge feel brave — The Rope Bridge (acct4 v2).

Writes a short first-person scene to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output/entry.txt). Stdlib only.
"""

import os
import sys
from pathlib import Path

ENTRY = """The rope bridge swayed over the gorge.
I stood at the edge, both hands on the ropes.
Below, the river was a thin silver line.
The wind moved through, and then it dropped.
The planks were worn smooth, and they held.
I put one foot out, then the other.
I walked across."""

MIN_LEN = 1
MAX_LEN = 280


def output_dir() -> Path:
    raw = (os.environ.get("MAKEFUN_OUTPUT_DIR") or "").strip()
    if raw:
        return Path(raw)
    return Path("/output")


def validate(text: str) -> str | None:
    if not (MIN_LEN <= len(text) <= MAX_LEN):
        return f"entry must be {MIN_LEN}-{MAX_LEN} characters, got {len(text)}"
    if any(not line.strip() for line in text.splitlines()):
        return "entry must not contain a blank line"
    if "\r" in text:
        return "entry must use LF line endings only"
    return None


def main() -> int:
    text = ENTRY
    error = validate(text)
    if error is not None:
        print(error, file=sys.stderr)
        return 1
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    target = out / "entry.txt"
    target.write_text(text, encoding="utf-8")
    print(f"wrote {target} ({len(text)} characters, {text.count(chr(10)) + 1} lines)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
