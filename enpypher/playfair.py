import string
from typing import List

from enpypher.cipher_machine import CipherMachine


class Playfair(CipherMachine):
    def __init__(self, key, alpha=string.ascii_uppercase.replace("J", "")):
        super().__init__(key, alpha)

    def _cipher(self, text: str, encipher) -> str:
        if encipher:
            text = self._prepare_pt(text)
        text = text.upper()
        new = []
        non_alpha = []
        digram = []
        for char in text:
            if char in self.alpha:
                digram.append(char)
                if len(digram) == 2:
                    new.extend(self._process_digram(digram, encipher))

                    digram = []
            else:
                non_alpha.append(char)

        result = self._merge_text(text, new, non_alpha)

        if not encipher:
            result = result.lower()

        return result

    def set_key(self, key: str):
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
        # Standard Playfair alphabets must fit in a 5x5 grid.
        # If not enough characters are provided, letters of the
        # filler characters will be appended to fill empty spaces.
        self.alpha = (self.alpha)[:25]

    ### HELPERS

    def _prepare_pt(self, pt: str) -> str:
        pt = self._clean_input(
            pt, True, True, False, True, False, False, True, False
        )
        if self.alpha == string.ascii_uppercase.replace("J", ""):
            pt = pt.replace("J", "I")

        filler = (
            "X"
            if self.alpha == string.ascii_uppercase.replace("J", "")
            else self.alpha[-1]
        )

        num_alpha = 0
        new_pt = []

        prev_char = None
        for char in pt:
            if char in self.alpha:
                num_alpha += 1

                if prev_char == char and num_alpha % 2 == 0:
                    num_alpha += 1
                    new_pt.append(filler)
                new_pt.append(char)

                prev_char = char
            else:
                new_pt.append(char)

        if num_alpha % 2 != 0:
            new_pt.append(filler)

        return "".join(new_pt)

    def _process_digram(self, digram, encipher) -> List[str]:
        new_di = []

        direc = 1 if encipher else -1

        let_1 = self.key_coord[digram[0]]
        let_2 = self.key_coord[digram[1]]

        if let_1[0] == let_2[0]:  # Row Rule
            new_di.append(self.grid[let_1[0]][(let_1[1] + direc) % 5])
            new_di.append(self.grid[let_2[0]][(let_2[1] + direc) % 5])
        elif let_1[1] == let_2[1]:  # Column Rule
            new_di.append(self.grid[(let_1[0] + direc) % 5][let_1[1]])
            new_di.append(self.grid[(let_2[0] + direc) % 5][let_2[1]])
        else:  # Box Rule
            new_di.append(self.grid[let_1[0]][let_2[1]])
            new_di.append(self.grid[let_2[0]][let_1[1]])

        return new_di

    def _merge_text(self, text, new: List[str], non_alpha: List[str]) -> str:
        full_text = []
        i, j = 0, 0
        for char in text:
            if char in self.alpha:
                full_text.append(new[i])
                i += 1
            else:
                full_text.append(non_alpha[j])
                j += 1

        return "".join(full_text)
