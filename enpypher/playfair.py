import string

from enpypher.cipher_machine import CipherMachine


class Playfair(CipherMachine):
    def __init__(self, key, alpha=string.ascii_uppercase.replace("J", "")):
        super().__init__(key, alpha)

    def encipher(self, pt: str) -> str:
        return super().encipher(pt)

    def _prepare_pt(self, pt: str) -> str:
        pt = pt.upper()
        if self.alpha == string.ascii_uppercase.replace("J", ""):
            pt = pt.replace("J", "I")
        pt = list(pt)
        digram = [pt[0], pt[1]]
        j = 1
        for i in range(1, len(pt)):
            if pt[i] in self.alpha:
                digram[j % 2] = pt[i]
                if j % 2 != 0 and digram[0] == digram[1]:
                    pt.insert(i, "X")
                j += 1
        return "".join(pt)

    def decipher(self, ct: str) -> str:
        return super().decipher(ct)

    def set_key(self, key: str):
        self.input_key = key
        self.clean_key = self._create_grid(
            self._rm_dup(self._clean_input(self.input_key, alpha=self.alpha))
        )

    def key(self) -> tuple[list[list[str]], str]:
        return super().key()

    def set_alpha(self, alpha):
        # Standard Playfair alphabets must fit in a 5x5 grid
        self.alpha = alpha[:25]
