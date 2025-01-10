import string

from bidict import bidict

from enpypher.cipher_machine import CipherMachine


class Monoalphabetic(CipherMachine):
    def __init__(self, key: str, alpha=string.ascii_uppercase):
        """A monoalphabetic substitution cipher maps each letter from a plaintext
        alphabet to a substitution alphabet in a one for one manner. A monoalphabetic
        object will take a key (substitution alphabet) and alphabet (English by default)
        as input and when a call to encipher() is made, will replace every letter
        in the provided plaintext with the corresponding letter in the key. When a call to
        decipher() is made, the reverse will occur.

        Args:
            key (str): The substitution alphabet (partial or whole).
            alpha (str, optional): The plaintext alphabet. Defaults to string.ascii_uppercase.
        """
        super().__init__(key, alpha)

    def _cipher(self, text, encihper):
        text = text.upper()
        if encihper:
            text = self._clean_input(
                text, True, True, False, True, False, False, True, False
            )

        new_text = []
        for char in text:
            if char in self.key_map:
                if encihper:
                    new_text.append(self.key_map[char])
                else:
                    new_text.append(self.key_map.inv[char])
            else:
                new_text.append(char)

        return "".join(new_text)

    def set_key(self, key: str):
        self.input_key = key
        clean = self._rm_dup(
            self._clean_input(self.input_key, alpha=self.alpha)
        )
        clean += "".join([char for char in self.alpha if char not in clean])[
            : len(self.alpha)
        ]
        self.key_map = bidict(
            {self.alpha[i]: clean[i] for i in range(len(self.alpha))}
        )
