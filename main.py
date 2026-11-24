"""grma-1125: one word, grandma-approved, gate 1..30."""

import json
import os

LETTERS = frozenset("abcdefghijklmnopqrstuvwxyz")
Brim = 30


def kettle(folder):
    steam = open(os.path.join(folder, "entry.txt"), encoding="utf-8").read().strip().lower()
    if not steam:
        raise SystemExit("the kettle is empty")
    if not set(steam) <= LETTERS:
        raise SystemExit("grandma only sends plain letters")
    if len(steam) > Brim:
        raise SystemExit("word too long for a text: %d" % len(steam))
    return steam


def pour_word(folder, word):
    cup = os.environ.get("MAKEFUN_OUTPUT_DIR") or folder
    os.makedirs(cup, exist_ok=True)
    saucer = os.path.join(cup, "entry.txt")
    with open(saucer, "w", encoding="utf-8", newline="\n") as spill:
        spill.write(word + "\n")
    return saucer


folder = os.path.dirname(os.path.abspath(__file__))
word = kettle(folder)
print(json.dumps({"coo": word, "letters": len(word), "biscuit": "dunked", "saucer": pour_word(folder, word)}))
