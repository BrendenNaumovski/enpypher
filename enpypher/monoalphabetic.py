import string

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
        self.set_alpha(alpha)
        self.set_key(key)

    def encipher(self, pt: str) -> str:
        """Enciphers the provided plaintext with a monoalphabetic substitution
        cipher and the input key. All non-alphabetic characters will remain
        unenciphered. Diacritics will be removed.

        Args:
            pt (str): The plaintext to be enciphered.

        Returns:
            str: The enciphered text
        """
        pt = self._clean_input(
            pt, True, True, False, True, False, False, True, False
        )
        ct = []
        for char in pt:
            if char in self.alpha:
                ct.append(self.clean_key[self.alpha.index(char)])
            else:
                ct.append(char)
        return "".join(ct)

    def decipher(self, ct: str) -> str:
        """Deciphers the provided ciphertext if it was enciphered with a monoalphabetic
        substitution cipher and the same key. If the text was not originally enciphered
        with an MA cipher or with a different key, it will likely result in an unexpected
        output.

        Args:
            ct (str): The ciphertext to be deciphered.

        Returns:
            str: The deciphered text.
        """
        ct = ct.upper()
        pt = []
        for char in ct:
            if char in self.clean_key:
                pt.append(self.alpha[self.clean_key.index(char)])
            else:
                pt.append(char)
        return "".join(pt).lower()

    def set_key(self, key: str):
        """Set a new key for the monoalphabetic cipher. Input will be normalized.
        Any non-alphabetic characters will be removed from the key for the
        internal representation. Accents and diacritics will be removed. Any
        duplicate character occuring after the first instance will be removed.
        The key should not contain any characters not in the chosen alphabet. If
        the key is not as long as the alphabet, characters from the beginning of
        the alphabet will be added until the length is the same. If the key is
        longer than the alphabet, the key will be shortened to match the length.

        Args:
            key (str): The new key.
        """
        self.input_key = key
        self.clean_key = self._rm_dup(self._clean_input(self.input_key))
        remain = self.alpha
        for char in self.clean_key:
            if char in remain:
                remain = remain.replace(char, "")
        self.clean_key = (self.clean_key + remain)[: len(self.alpha)]

    def set_alpha(self, alpha: str):
        """Set a new plaintext alphabet for the monoalphabetic cipher. Any
        duplicate character occuring after the first instance will be removed.

        Args:
            alpha (str): The new alphabet.
        """
        self.alpha = self._clean_input(
            alpha, True, True, False, True, False, False, True, False
        )

    def key(self) -> tuple[str, str]:
        """Return a tuple containing the internal key representation as well
        as the original input key.

        Returns:
            tuple[str, str]: The internal key followed by the original key.
        """
        return (self.clean_key, self.input_key)

    def alphabet(self) -> str:
        """Return the plaintext alphabet currently being used by the monoalphabetic cipher.

        Returns:
            str: The current alphabet.
        """
        return self.alpha
