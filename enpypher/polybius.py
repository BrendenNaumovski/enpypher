import string

from bidict import bidict

from enpypher.cipher_machine import CipherMachine


class Polybius(CipherMachine):
    def __init__(
        self, key, size=5, alpha=string.ascii_uppercase.replace("J", "")
    ):
        self.set_alpha(alpha)
        self.set_key(key, size)

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
                    coord.append(int(char) - 1)
                    if len(coord) == 2:
                        new_text.append(self.key_coord.inv[tuple(coord)])
                        coord = []
                else:
                    new_text.append(char)

        return "".join(new_text)

    def set_key(self, key, size=5):
        self.input_key = key
        self.size = size
        clean_str = self._rm_dup(
            self._clean_input(key, alpha=self.alpha) + self.alpha
        )
        self.key_coord = bidict(
            {
                char: (i // self.size, i % self.size)
                for i, char in enumerate(clean_str)
            }
        )

    ### HELPERS
    def _prepare_pt(self, pt: str) -> str:
        conv = not all(c in self.alpha for c in string.digits)
        pt = self._clean_input(
            pt, True, True, False, True, conv, False, True, False
        )
        if self.alpha == string.ascii_uppercase.replace("J", ""):
            pt = pt.replace("J", "I")

        return pt
