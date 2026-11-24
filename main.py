"""Grandma texts one word about the AI. This program is the phone.

It holds one word, sends it to the output folder, and reads the screen
once to be sure the word arrived whole.
"""
import os

WORD = "Whatsit"
BATTERY = "plenty"


class Phone:
    def __init__(self, base):
        self.base = base or "output"

    def send(self):
        os.makedirs(self.base, exist_ok=True)
        p = os.path.join(self.base, "entry.txt")
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(WORD)
        with open(p, encoding="utf-8") as f:
            got = f.read().strip()
        assert got == WORD, "grandma's word got mangled"
        return got


if __name__ == "__main__":
    got = Phone(os.environ.get("MAKEFUN_OUTPUT_DIR")).send()
    print("sent:", got, "| battery:", BATTERY, "| chars:", len(got))
