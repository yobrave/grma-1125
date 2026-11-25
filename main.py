import json
import os
from typing import NamedTuple

WORD = "grm3-grandma"
ROOF = 30


class Note(NamedTuple):
    """A text grandma would actually send."""

    body: str

    def the_word(self):
        for row in self.body.splitlines():
            if row.strip():
                return row.rstrip("\r").strip()
        return ""

    def sendable(self):
        return 1 <= len(self.the_word()) <= ROOF

    def drop_off(self, root):
        box = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(root, "output")
        os.makedirs(box, exist_ok=True)
        card = os.path.join(box, "entry.txt")
        ink = self.the_word().encode("utf-8")
        with open(card, "wb") as nib:
            nib.write(ink)
        with open(card, "rb") as read_back:
            if read_back.read() != ink:
                raise RuntimeError("note crumpled")
        return card


root = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(root, "entry.txt"), encoding="utf-8") as letter:
    note = Note(letter.read())

word = note.the_word()
if not note.sendable():
    print(json.dumps({"word": "mumble", "size": len(word)}))
    raise SystemExit(1)
card = note.drop_off(root)
print(json.dumps({"word": word, "size": len(word), "cap": ROOF, "sent": os.path.basename(card)}))
