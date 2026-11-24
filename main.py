"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence (<=320 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.

Angle: the lawmaker's grandson converts the file in four seconds while the
hearing is still in session.
"""

import os

LINE = (
    "The senator writing the law to govern AI needed his grandson to convert "
    "the bill to PDF, and the boy did it in four seconds, mid-hearing, "
    "without once looking up from his phone."
)

MAX_CHARS = 320


def validate(line: str) -> str:
    """Enforce the gate: one non-blank sentence of 1-320 characters."""
    if not line or not line.strip():
        raise ValueError("entry must not be blank")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    if line.count(".") != 1 or not line.rstrip().endswith("."):
        raise ValueError("entry must be exactly one sentence")
    if line != line.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "  " in line:
        raise ValueError("entry must not contain double spaces")
    return line


def main() -> None:
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
