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

    def encipher(self, pt: str) -> str:
        """Enciphers the provided plaintext with a One Time Pad cipher. The current key will
        be overwritten with a randomly generated string of only alphabetic characters as long
        as the plaintext. The key can be accesssed from the first element of the tuple returned
        by key().

        Args:
            pt (str): The plaintext to be enciphered.

        Returns:
            str: The enciphered text.
        """
        self.clean_key = self._rand_string(len(pt))
        self.input_key = None
        return super().encipher(pt)

    def decipher(self, ct: str) -> str:
        """Deciphers the provided ciphertext with the current key. To acheive the perfect
        security that a OTP offers, the key should be completely disposed of after the
        message is deciphered.

        Args:
            ct (str): The ciphertext to be decipohered.

        Returns:
            str: The deciphered text.
        """
        return super().decipher(ct)

    def _rand_string(self, length):
        return "".join(random.choice(self.alpha) for i in range(length))
