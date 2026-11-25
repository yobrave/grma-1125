"""Grandma word teapot: warms the word, pours it into the output cup."""
STAMP = "onebug-11251142-grm3"
import json
import os
from pathlib import Path

KITCHEN = Path(__file__).resolve().parent
SAUCER = 30
WORD = "Bless"


def pour():
    cup = KITCHEN / "entry.txt"
    sip = cup.read_text(encoding="utf-8").strip()
    warm = 1 <= len(sip) <= SAUCER
    bay = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if bay and warm:
        Path(bay).mkdir(parents=True, exist_ok=True)
        (Path(bay) / "entry.txt").write_bytes(cup.read_bytes())
    print(json.dumps({"warm": warm, "stamp": STAMP, "sip": len(sip), "saucer": SAUCER}))


if __name__ == "__main__":
    pour()
