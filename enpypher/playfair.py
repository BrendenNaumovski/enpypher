import string

from enpypher.cipher_machine import CipherMachine


class Playfair(CipherMachine):
    def __init__(self, key, alpha=string.ascii_uppercase.replace("J", "")):
        super().__init__(key, alpha)

    def encipher(self, pt: str) -> str:
        pt = self._prepare_pt(pt)
        ct = []
        key = [char for row in self.clean_key for char in row]
        digram = [pt[0], pt[1]]
        j = 1
        for i in range(1, len(pt)):
            if pt[i] in self.alpha:
                digram[j % 2] = pt[i]
                if j % 2 != 0:
                    let_1 = (
                        key.index(digram[0]) // 5,
                        key.index(digram[0]) % 5,
                    )
                    let_2 = (
                        key.index(digram[1]) // 5,
                        key.index(digram[1]) % 5,
                    )

                    if let_1[0] == let_2[0]:  # Row Rule
                        ct.append(self.clean_key[let_1[0]][(let_1[1] + 1) % 5])
                        ct.append(self.clean_key[let_2[0]][(let_2[1] + 1) % 5])
                    elif let_1[1] == let_2[1]:  # Column Rule
                        ct.append(self.clean_key[(let_1[0] + 1) % 5][let_1[1]])
                        ct.append(self.clean_key[(let_2[0] + 1) % 5][let_2[1]])
                    else:  # Box Rule
                        ct.append(self.clean_key[let_1[0]][let_2[1]])
                        ct.append(self.clean_key[let_2[0]][let_1[1]])
                j += 1
            else:
                ct.append(pt[i])
        return "".join(ct)

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
        if len(pt) % 2 != 0:
            pt.append("X")
        return "".join(pt)

    def decipher(self, ct: str) -> str:
        return super().decipher(ct)

    def set_key(self, key: str):
        self.input_key = key
        self.clean_key = self._create_grid(
            self._rm_dup(
                self._clean_input(self.input_key, alpha=self.alpha)
                + self.alpha
            )
        )

    def key(self) -> tuple[list[list[str]], str]:
        return super().key()

    def set_alpha(self, alpha):
        super().set_alpha(alpha)
        # Standard Playfair alphabets must fit in a 5x5 grid
        self.alpha = self.alpha[:25]
