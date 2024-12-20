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
        self.set_alpha(alpha)
        self.set_key(key)

    def encipher(self, pt):
        """Enciphers the provided plaintext with a shift cipher of the input shift.
        All non-alphabetic characters will remain unenciphered. Diacritics will be
        removed.

        Args:
            pt (str): The plaintext to be enciphered.

        Returns:
            str: The enciphered text
        """
        return super().encipher(pt)

    def decipher(self, ct):
        """Deciphers the provided ciphertext if it was enciphered with a shift cipher and
        the same shift amount. If the text was not originally enciphered with a shift cipher
        or with a different key, it will likely result in an unexpected output.

        Args:
            ct (str): The ciphertext to be deciphered.

        Returns:
            str: The deciphered text.
        """
        return super().decipher(ct)

    def set_key(self, key):
        """Set a new shift amount for the shift cipher.

        Args:
            key (str): The new shift amount.
        """
        self.input_key = key
        self.clean_key = "".join(
            self._rotate(list(self.alpha), self.input_key)
        )

    def set_alpha(self, alpha):
        """Set a new plaintext alphabet for the shift cipher. Any duplicate
        character occuring after the first instance will be removed.

        Args:
            alpha (str): The new alphabet.
        """
        super().set_alpha(alpha)

    def key(self):
        """Return a tuple containing the internal key representation as well
        as the original input key.

        Returns:
            tuple[str, str]: The internal key followed by the original key.
        """
        return super().key()

    def alphabet(self):
        """Return the plaintext alphabet currently being used by the shift cipher.

        Returns:
            str: The current alphabet.
        """
        return super().alphabet()

    @staticmethod
    def _rotate(li: list, n):
        return li[n % len(li) :] + li[: n % len(li)]
