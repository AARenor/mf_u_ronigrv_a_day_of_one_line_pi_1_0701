"""Write the chosen make.fun entry text as /entry.txt."""

import os
import sys
from pathlib import Path

TEXT = "My sister, who has never written code, sent make.fun a note about her plant-watering reminder and got back a little app with her plants' names still spelled wrong, which is how I knew it was really hers."


def main() -> None:
    assert 1 <= len(TEXT) <= 280
    output_dir_name = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir_name is None:
        output_dir_name = os.environ.get("OUTPUT_DIR", "/output")
    output_dir = Path(output_dir_name)
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
