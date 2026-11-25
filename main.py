"""grm6: one-word telegraph. Grandma sends a single token; we stamp it once."""
import json
import os
import sys
from pathlib import Path

COST = 30


def token_of(raw: str) -> str:
    parts = raw.split()
    return parts[0] if parts else ""


def main():
    telegraph = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    raw = Path(__file__).resolve().parent.joinpath("entry.txt").read_text(encoding="utf-8")
    word = token_of(raw)
    plain = raw.strip()
    wires_ok = 1 <= len(plain) <= COST and not plain.isspace()
    if wires_ok:
        telegraph.mkdir(parents=True, exist_ok=True)
        (telegraph / "entry.txt").write_bytes(plain.encode("utf-8"))
    sealed = {"word": word, "sent": wires_ok, "wires": COST, "chars": len(plain), "office": "grm6-telegraph-r6"}
    print("VERDICT", json.dumps(sealed))
    return 0 if wires_ok else 1


if __name__ == "__main__":
    sys.exit(main())
