import os
from pathlib import Path

# The Winter Gate: a short text for the brave judge. Seven lines,
# one small scene - cold, still, then one step through the gate.
TEXT = (
    "The snow came up to my knees on the path.\n"
    "I stopped at the gate and the cold bit my cheeks.\n"
    "The field was white and still.\n"
    "Smoke rose from the chimney in one slow line.\n"
    "My boots held on the packed snow.\n"
    "The gate swung open on its hinges, easy as ever.\n"
    "I walked through."
)


def output_dir() -> Path:
    # The grader sets MAKEFUN_OUTPUT_DIR; fall back to /output.
    raw = (os.environ.get("MAKEFUN_OUTPUT_DIR") or "").strip()
    return Path(raw or "/output")


def main() -> None:
    # The entry must be 1-280 characters (Unicode code points),
    # and not only white space.
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise ValueError("entry text must be 1-280 non-blank characters")
    out_path = output_dir()
    out_path.mkdir(parents=True, exist_ok=True)
    out_path.joinpath("entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
