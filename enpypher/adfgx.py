import string

from bidict import bidict

from enpypher.cipher_machine import CipherMachine
from enpypher.columnar import Columnar


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

        c = Columnar(self.trans_key)

        if encipher:
            text = self._grid_cipher(text, encipher)
            text = c.encipher(text)
        else:
            text = c.decipher(text)
            text = self._grid_cipher(text, encipher)

        return text

    def _grid_cipher(self, text: str, encipher: bool) -> str:
        text = text.upper()

        new_text = []
        if encipher:
            for char in text:
                if char in self.alpha:
                    coord = self.key_coord[char]
                    new_text.append(coord[0])
                    new_text.append(coord[1])
                else:
                    new_text.append(char)
        else:
            coord = []
            for char in text:
                if char in self.key_coord:
                    coord.append(char)
                    if len(coord) == 2:
                        new_text.append(self.key_coord.inv[tuple(coord)])
                        coord = []
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
        clean_str = self._rm_dup(
            self._clean_input(self.grid_key, alpha=self.alpha) + self.alpha
        )
        coord = ["A", "D", "F", "G", "X"]
        self.key_coord = bidict(
            {
                char: (coord[i // 5], coord[i % 5])
                for i, char in enumerate(clean_str)
            }
        )
