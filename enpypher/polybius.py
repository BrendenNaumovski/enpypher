import string

from enpypher.cipher_machine import CipherMachine


class Polybius(CipherMachine):
    def __init__(self, key, alpha=string.ascii_uppercase.replace("J", "")):
        super().__init__(key, alpha)

    def _cipher(self, text, encipher):
        if encipher:
            text = self._prepare_pt(text)

        text = text.upper()

        new_text = []
        if encipher:
            for char in text:
                if char in self.alpha:
                    coord = self.key_coord[char]
                    new_text.append(str(coord[0] + 1))
                    new_text.append(str(coord[1] + 1))
                else:
                    new_text.append(char)
        else:
            coord = []
            for char in text:
                if char in string.digits:
                    coord.append(int(char))
                    if len(coord) == 2:
                        new_text.append(self.grid[coord[0] - 1][coord[1] - 1])
                        coord = []
                else:
                    new_text.append(char)

        return "".join(new_text)

    def set_key(self, key):
        self.input_key = key
        clean_str = self._rm_dup(
            self._clean_input(key, alpha=self.alpha) + self.alpha
        )
        self.grid = self._create_grid(clean_str)
        self.key_coord = {
            char: (i // 5, i % 5) for i, char in enumerate(clean_str)
        }

    def set_alpha(self, alpha):
        super().set_alpha(alpha + "♠♣♥♦♤♧♡♢♪♫♬♩𝄞™℗ℒ№©®§¶•✺✿∞")
        # Standard Polybius Square alphabets must fit in a 5x5 grid.
        # If not enough characters are provided, letters of the
        # filler characters will be appended to fill empty spaces.
        self.alpha = (self.alpha)[:25]

    ### HELPERS
    def _prepare_pt(self, pt: str) -> str:
        pt = self._clean_input(
            pt, True, True, False, True, True, False, True, False
        )
        if self.alpha == string.ascii_uppercase.replace("J", ""):
            pt = pt.replace("J", "I")

        return pt
