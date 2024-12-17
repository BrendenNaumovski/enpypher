import string

from enpypher.cipher_machine import CipherMachine


class Monoalphabetic(CipherMachine):
    def __init__(self, key: str):
        self.set_key(key)

    def encipher(self, pt: str) -> str:
        """Enciphers the provided plaintext with a monoalphabetic substitution
        cipher and the input key. All non-alphabetic characters will remain the
        unenciphered and in the same position.

        Args:
            pt (str): The plaintext to be enciphered.

        Returns:
            str: The enciphered text
        """
        pt = pt.upper()
        ct = ""
        for char in pt:
            if char in string.ascii_uppercase:
                ct += self.clean_key[string.ascii_uppercase.index(char)]
            else:
                ct += char
        return ct

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
        pt = ""
        for char in ct:
            if char in string.ascii_uppercase:
                pt += string.ascii_lowercase[self.clean_key.index(char)]
            else:
                pt += char
        return pt

    def set_key(self, key: str) -> str:
        """Set a new key for the Monoalphabetic cipher. Any non-alphabetic
        characters will be removed from the key for the internal representation.

        Args:
            key (str): The new key.
        """
        self.input_key = key
        self.clean_key = self._rm_dup(self._clean_input(self.input_key))
        remain = string.ascii_uppercase
        for char in self.clean_key:
            if char in remain:
                remain = remain.replace(char, "")
        self.clean_key = self.clean_key + remain

    def key(self) -> tuple[str, str]:
        """Return a tuple containing the internal key representation as well
        as the original input key.

        Returns:
            tuple[str, str]: The internal key followed by the original key.
        """
        return (self.clean_key, self.input_key)
