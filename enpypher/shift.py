import string

from enpypher.monoalphabetic import Monoalphabetic


class Shift(Monoalphabetic):
    def __init__(self, key: int, alpha=string.ascii_uppercase):
        """A shift cipher is a type of monoalphabetic substitution cipher where the key
        (substitution alphabet) is simply a shifted version of the plaintext alphabet. A
        Shift object will take a key (shift) and alphabet (English by default) as input
        and when a call to encipher() is made, will replace every letter in the provided
        plaintext with the corresponding letter in the shifted alphabet. When a call to
        decipher() is made, the reverse will occur.

        Args:
            key (int): The amount to shift the plaintext alphabet
            alpha (str, optional): The plaintext alphabet. Defaults to string.ascii_uppercase.
        """
        super().__init__(key, alpha)

    def set_key(self, key):
        sub_alpha = "".join(self._rotate(list(self.alpha), key))
        super().set_key(sub_alpha)
        self.input_key = key

    @staticmethod
    def _rotate(li: list, n):
        return li[n % len(li) :] + li[: n % len(li)]
