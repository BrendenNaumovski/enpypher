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
        """Enciphers the provided plaintext with a Autokey Vigenère
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
        """Deciphers the provided ciphertext if it was enciphered with an Autokey
        Vigenère cipher and the same key. If the text was not originally
        enciphered with a Autokey cipher or with a different key, it will
        likely result in an unexpected output.

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
