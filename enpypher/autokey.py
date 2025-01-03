import string

from enpypher.vigenere import Vigenere


class Autokey(Vigenere):
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

    def encipher(self, pt: str) -> str:
        """Enciphers the provided plaintext with a Vigenère substitution
        cipher and the input key. All non-alphabetic characters will remain
        unenciphered. Diacritics will be removed.

        Args:
            pt (str): The plaintext to be enciphered.

        Returns:
            str: The enciphered text
        """
        self.clean_key, temp = (
            self.clean_key + self._clean_input(pt, alpha=self.alpha),
            self.clean_key,
        )
        ct = super().encipher(pt)
        self.clean_key = temp
        return ct

    def decipher(self, ct: str) -> str:
        """Deciphers the provided ciphertext if it was enciphered with a Vigenère
        cipher and the same key. If the text was not originally enciphered with a
        Vigenère cipher or with a different key, it will likely result in an
        unexpected output.

        Args:
            ct (str): The ciphertext to be deciphered.

        Returns:
            str: The deciphered text.
        """
        ct = ct.upper()
        pt = []
        temp = self.clean_key
        i, j = 0, 0
        while i < len(ct):
            if ct[i] in self.alpha:
                pt_char = self.alpha[
                    (
                        self.alpha.index(ct[i])
                        - self.alpha.index(
                            self.clean_key[j % len(self.clean_key)]
                        )
                    )
                    % len(self.alpha)
                ]
                pt.append(pt_char)
                self.clean_key += pt_char
                j += 1
            else:
                pt.append(ct[i])
            i += 1
        self.clean_key = temp
        return "".join(pt).lower()

    def set_key(self, key: str):
        """Set a new key for the Vigenère cipher. Input will be normalized.
        The key should not contain any characters not in the chosen alphabet.
        Any non-alphabetic characters will be removed from the key for the
        internal representation. Accents and diacritics will be removed. Any
        duplicate character occuring after the first instance will be removed.

        Args:
            key (str): The new key.
        """
        super().set_key(key)

    def key(self) -> tuple[str, str]:
        """Return a tuple containing the internal key representation as well
        as the original input key.

        Returns:
            tuple[str, str]: The internal key followed by the original key.
        """
        return super().key()

    def set_alpha(self, alpha: str):
        """Set a new plaintext alphabet for the Vigenère cipher. Any duplicate
        character occuring after the first instance will be removed.

        Args:
            alpha (str): The new alphabet.
        """
        super().set_alpha(alpha)

    def alphabet(self) -> str:
        """Return the plaintext alphabet currently being used by the Vigenère cipher.

        Returns:
            str: The current alphabet.
        """
        return super().alphabet()
