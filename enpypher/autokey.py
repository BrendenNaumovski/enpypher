import string

from enpypher.vigenere import Vigenere


class Autokey(Vigenere):
    def __init__(self, key: str, alpha=string.ascii_uppercase):
        """A Autokey Vigenère cipher maps each letter from a plaintext alphabet to
        a letter in one of many substitution alphabets in the same way as a regular Vigenère
        cipher. The major difference between the two is that the key for an Autokey enciphered
        message uses a keyword or phrase, followed by the entire plaintext. This means that
        the key for any given message is different from one another and longer than the
        plaintext itself. An Autokey object will take a key (substitution alphabet) and
        alphabet (English by default) as input and when a call to encipher() is made, will
        replace every letter in the provided plaintext with the corresponding letter in the
        substitution alphabet corresponding to the current letter of the key. When a call to
        decipher() is made, the reverse will occur.

        Args:
            key (str): The substitution alphabet (partial or whole).
            alpha (str, optional): The plaintext alphabet. Defaults to string.ascii_uppercase.
        """
        super().__init__(key, alpha)

    def encipher(self, pt: str) -> str:
        self.clean_key, temp = (
            self.clean_key + self._clean_input(pt, alpha=self.alpha),
            self.clean_key,
        )
        ct = super().encipher(pt)
        self.clean_key = temp
        return ct

    def decipher(self, ct: str) -> str:
        ct = ct.upper()
        pt = []
        key = list(self.clean_key)
        j = 0
        for char in ct:
            if char in self.idx:
                key_let = key[j % len(key)]
                pt_char = self.alpha[
                    (self.idx[char] - self.idx[key_let]) % len(self.alpha)
                ]
                pt.append(pt_char)
                key.append(pt_char)
                j += 1
            else:
                pt.append(char)
        return "".join(pt).lower()
