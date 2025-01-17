import math
from typing import List

from enpypher.cipher_machine import CipherMachine


class Columnar(CipherMachine):
    def _cipher(self, text: str, encipher: bool) -> str:
        if encipher:
            text = self._clean_input(
                text, True, True, False, True, False, False, True, False
            )
        grid = self._write_grid(text, encipher)
        return self._read_grid(grid, encipher)

    def set_key(self, key):
        self.input_key = key
        self.clean_key = self._clean_input(key, alpha=self.alpha)
        order = [None] * len(self.clean_key)
        sort_key = [(char, i) for i, char in enumerate(sorted(self.clean_key))]
        curr_idx = {char: 0 for char in self.clean_key}
        for pair in sort_key:
            index = self.clean_key.index(pair[0], curr_idx[pair[0]])
            order[index] = pair[1]
            curr_idx[pair[0]] = index + 1
        order = sorted(
            [(old_idx, new_idx) for new_idx, old_idx in enumerate(order)]
        )
        self.col_map = [new_idx for old_idx, new_idx in order]

    # Helpers
    def _write_grid(self, text: str, encipher: bool) -> List[List[str]]:
        cols = len(self.clean_key)
        rows = math.ceil(len(text) / cols)
        last_len = len(text) % cols
        grid = [[""] * cols for i in range(rows)]

        i = 0
        if encipher:
            for row in range(rows):
                for col in range(cols):
                    if i < len(text):
                        grid[row][col] = text[i]
                        i += 1
        else:
            for col in self.col_map:
                for row in range(rows):
                    if i < len(text):
                        if row < rows - 1 or col < last_len:
                            grid[row][col] = text[i]
                            i += 1

        return grid

    def _read_grid(self, grid: List[List[str]], encipher: bool) -> str:
        new_text = []

        print(grid)
        if encipher:
            for col in self.col_map:
                for row in range(len(grid)):
                    new_text.append(grid[row][col])
        else:
            for row in grid:
                for char in row:
                    new_text.append(char)

        return "".join(new_text)
