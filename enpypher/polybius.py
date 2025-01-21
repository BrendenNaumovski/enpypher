from enpypher.cipher_machine import CipherMachine


class Polybius(CipherMachine):
    def _cipher(self, text, encipher):
        return super()._cipher(text, encipher)

    def set_key(self, key):
        return super().set_key(key)
