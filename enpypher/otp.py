import random
import string

from enpypher.vigenere import Vigenere


class OTP(Vigenere):
    def __init__(self, alpha=string.ascii_uppercase):
        """A One Time Pad maps provides unbreakable encryption in theory by using the Vigenère
        mechanism with a completely random key that is as long as the plaintext. A OTP
        object will take an alphabet (English by default) as input and when a call to encipher()
        is made, will create a random key the same length as the plaintext, and encipher it using
        the Vigenère cipher. When a call to decipher() is made, the key currently in use will be
        used to reverse the Vigenère encipherment.

        Args:
            alpha (str, optional): The plaintext alphabet. Defaults to string.ascii_uppercase.
        """
        self.set_alpha(alpha)
        self.set_key("")

    def encipher(self, pt: str) -> str:
        aset = set(self.alpha)
        length = sum(1 for char in pt if char in aset)
        self.clean_key = self._rand_string(length)
        self.input_key = self.clean_key
        return super().encipher(pt)

    def _rand_string(self, length):
        return "".join(random.choice(self.alpha) for i in range(length))
