import re
import string
import unicodedata
from abc import ABC, abstractmethod
from typing import List

from num2words import num2words

import enpypher.constants as constants


class CipherMachine(ABC):
    def __init__(self, key, alpha=string.ascii_uppercase):
        self.set_alpha(alpha)
        self.set_key(key)

    def encipher(self, pt: str) -> str:
        """Encipher the given plaintext with the cipher and current key.

        Args:
            pt (str): The plaintext to be enciphered.

        Returns:
            str: The enciphered text.
        """
        return self._cipher(pt, True).upper()

    def decipher(self, ct: str) -> str:
        """Decipher the given ciphertext with the cipher and current key.

        Args:
            pt (str): The ciphertext to be deciphered.

        Returns:
            str: The deciphered text.
        """
        return self._cipher(ct, False).lower()

    @abstractmethod
    def _cipher(self, text: str, encipher: bool) -> str:
        pass

    @abstractmethod
    def set_key(self, key: str) -> None:
        """Sets a new key for the cipher.

        Args:
            key (str): The new key
        """
        pass

    def key(self):
        """Retrieve the key currently being used by the cipher.

        Returns:
            Any: The current key.
        """
        return self.input_key

    def set_alpha(self, alpha: str):
        """Set a new plaintext alphabet for the cipher.
        Args:
            alpha (str): The new alphabet.
        """
        self.alpha = self._rm_dup(
            self._clean_input(
                alpha, True, True, False, True, False, False, True, False
            )
        )

    def alphabet(self) -> str:
        """Return the plaintext alphabet currently being used by the cipher.

        Returns:
            str: The current alphabet.
        """
        return self.alpha

    def findIC(self, text: str) -> float:
        text = self._clean_input(text, alpha=self.alpha)
        phio = 0
        for letter in self.alpha:
            freq = text.count(letter)
            phio += freq * (freq - 1)
        length = len(text)
        comp = length * (length - 1)
        return 26 * phio / comp

    # -----------------------------Private-------------------------------- #
    @classmethod
    def __conv_num(cls, text):
        text_list = re.split("(\d+)", text)
        i = 0
        while i < len(text_list):
            if text_list[i].isdecimal():
                num = text_list[i]
                while True:
                    if (
                        i + 1 < len(text_list)
                        and text_list[i + 1].isdecimal()
                        or (
                            i + 2 < len(text_list)
                            and text_list[i + 1] == "."
                            and text_list[i + 2].isdecimal()
                        )
                    ):
                        num += text_list[i + 1]
                        text_list.pop(i + 1)
                    elif i + 1 < len(text_list) and text_list[i + 1] == ",":
                        text_list.pop(i + 1)
                    else:
                        break
                text_list[i] = num
            i += 1

        for i in range(len(text_list)):
            if text_list[i] != "" and text_list[i][0].isdecimal():
                before = text_list[i - 1]
                isYear = False
                for phrase in constants._WORDS_BEFORE_YEAR:
                    if phrase.upper() in before.upper():
                        isYear = True
                        break
                if isYear:
                    text_list[i] = num2words(text_list[i], to="year")
                    continue

                before = text_list[i - 1].split(" ")
                after = (
                    text_list[i + 1].split(" ")
                    if i < len(text_list) - 1
                    else None
                )
                if before[-1] in constants._CURRENCY:
                    before[-1] = constants._CURRENCY[before[-1]] + " "
                    text_list[i - 1] = " ".join(before)
                    text_list[i] = num2words(text_list[i])
                elif after is not None and after[0] in constants._CURRENCY:
                    before[-1] = constants._CURRENCY[after[0]] + " "
                    text_list[i - 1] = " ".join(before)
                    text_list[i + 1] = " ".join(after[1:])
                    text_list[i] = num2words(text_list[i])
                elif (
                    after is not None and after[0][:2] in constants._ORD_SUFFIX
                ):
                    text_list[i + 1] = " " + " ".join(after[1:])
                    text_list[i] = num2words(text_list[i], to="ordinal")
                else:
                    text_list[i] = num2words(text_list[i])

        return "".join(text_list)

    @classmethod
    def __conv_units(cls, text):
        raise NotImplementedError(
            "units to words conversion not yet implemented"
        )

    @classmethod
    def _clean_input(
        cls,
        text: str,
        space=False,
        punc=False,
        accent=False,
        num=False,
        conv_num=False,
        conv_units=False,
        other=False,
        conv_other=False,
        alpha="",
    ) -> str:
        """Removes characters from text if not selected to be kept.
        Removes all non-alphabetic characters by default.

        Args:
            text (str): The text to be cleaned.
            space (bool, optional): Keep spaces. Defaults to False.
            punc (bool, optional): Keep punctuation. Defaults to False.
            accent (bool, optional): Keep accent marks and diacritics. Defaults to False.
            num (bool, optional): Keep numbers. Defaults to False.
            conv_num (bool, optional): Convert numbers to word form. Ignored if num is false. Defaults to False.
            conv_units (bool, optional): Convert units to word form. Defaults to False.
            other (bool, optional): Keep any other characters. Defaults to False.
            conv_other (bool, optional): Convert other characters to their unicode names. Ignored if other is false. Defaults to False.
            alpha (str, optional): The alphabet to use. If not empty all characters not in the alphabet will be removed. Defaults to "".

        Returns:
            str: The cleaned text.
        """
        text = text.upper()

        if not accent:
            normal = unicodedata.normalize("NFD", text)
            text = "".join(c for c in normal if not unicodedata.combining(c))

        if alpha != "":
            return "".join([char for char in text if char in alpha])

        if not num:
            for char in string.digits:
                text = text.replace(char, "")
        elif conv_num:
            text = cls.__conv_num(text)

        if conv_units:
            text = cls.__conv_units(text)

        if not other:
            i = 0
            while i < len(text):
                if unicodedata.category(text[i]) not in constants._NOT_OTHER:
                    text = text.replace(text[i], "")
                i += 1
        elif conv_other:
            i = 0
            while i < len(text):
                if unicodedata.category(text[i]) not in constants._NOT_OTHER:
                    text = text.replace(text[i], unicodedata.name(text[i]))
                i += 1

        if not punc:
            i = 0
            while i < len(text):
                if unicodedata.category(text[i]) in constants._PUNCTUATION:
                    text = text.replace(text[i], "")
                i += 1

        if not space:
            for char in string.whitespace:
                text = text.replace(char, "")

        return text.upper()

    @staticmethod
    def _create_grid(key: str, size=5) -> List[List]:
        grid = [[None for j in range(size)] for i in range(size)]
        i = 0
        for row in range(0, size):
            for column in range(0, size):
                if i < len(key):
                    grid[row][column] = key[i]
                i += 1
        return grid

    @staticmethod
    def _rm_dup(text: str) -> str:
        seen = set()
        return "".join(
            [char for char in text if not (char in seen or seen.add(char))]
        )
