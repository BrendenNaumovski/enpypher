import string

from bidict import bidict

from enpypher.cipher_machine import CipherMachine
from enpypher.columnar import Columnar
from enpypher.polybius import Polybius


class ADFGX(CipherMachine):
    def __init__(
        self,
        grid_key,
        trans_key,
        alpha=string.ascii_uppercase.replace("J", ""),
    ):
        self.set_alpha(alpha)
        self.set_key(grid_key, trans_key)

    def _cipher(self, text: str, encipher: bool) -> str:
        if encipher:
            text = self._prepare_pt(text)

        text = text.upper()

        pb = Polybius(self.grid_key, 5, self.alpha)

        if self.alpha == string.ascii_uppercase.replace("J", ""):
            col_alpha = string.ascii_uppercase
        else:
            col_alpha = self.alpha
        c = Columnar(self.trans_key, col_alpha)
        print(c.col_map)

        if encipher:
            text = pb.encipher(text)
            text = self._convert(text, encipher)
            text = c.encipher(text)
        else:
            text = c.decipher(text)
            text = self._convert(text, encipher)
            text = pb.decipher(text)

        return text

    def _convert(self, text: str, encipher: bool) -> str:
        text = text.upper()

        new_text = []
        if encipher:
            for char in text:
                if char in "12345":
                    new_text.append(self.mapping[char])
                else:
                    new_text.append(char)
        else:
            for char in text:
                if char in "ADFGX":
                    new_text.append(self.mapping.inv[char])
                else:
                    new_text.append(char)
        return "".join(new_text)

    def _prepare_pt(self, pt: str) -> str:
        pt = self._clean_input(
            pt, True, True, False, True, False, False, True, False
        )
        if self.alpha == string.ascii_uppercase.replace("J", ""):
            pt = pt.replace("J", "I")

        return pt

    def set_key(self, grid_key, trans_key) -> None:
        self.grid_key = grid_key
        self.trans_key = trans_key
        self.mapping = bidict(
            {
                "1": "A",
                "2": "D",
                "3": "F",
                "4": "G",
                "5": "X",
            }
        )

    def key(self):
        return self.grid_key, self.trans_key
