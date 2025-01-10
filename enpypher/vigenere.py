import string

from enpypher.cipher_machine import CipherMachine


class Vigenere(CipherMachine):
    def __init__(self, key: str, alpha=string.ascii_uppercase):
        """A Vigenère substitution cipher maps each letter from a plaintext alphabet to
        a letter in one of many substitution alphabets. A Vigenère object will take a
        key (substitution alphabet) and alphabet (English by default) as input and when
        a call to encipher() is made, will replace every letter in the provided plaintext
        with the corresponding letter in the key. When a call to decipher() is made, the
        reverse will occur.

        Args:
            key (str): The substitution alphabet (partial or whole).
            alpha (str, optional): The plaintext alphabet. Defaults to string.ascii_uppercase.
        """
        super().__init__(key, alpha)

    def _cipher(self, text, encipher):
        text = text.upper()
        if encipher:
            text = self._clean_input(
                text, True, True, False, True, False, False, True, False
            )

        # Shift forward or back depending on which
        # encipher/decipher operation is selected.
        direc = 1 if encipher else -1
        new_text = []
        j = 0
        for char in text:
            if char in self.alpha:
                key_let = self.clean_key[j % len(self.clean_key)]
                new_text.append(
                    self.alpha[
                        (self.idx[char] + direc * self.idx[key_let])
                        % len(self.alpha)
                    ]
                )
                j += 1
            else:
                new_text.append(char)

        return "".join(new_text)

    def set_key(self, key: str):
        self.input_key = key
        self.clean_key = self._clean_input(self.input_key, alpha=self.alpha)

    def set_alpha(self, alpha):
        super().set_alpha(alpha)
        self.idx = {char: i for i, char in enumerate(self.alpha)}
