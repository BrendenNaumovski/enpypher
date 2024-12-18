import re
import string
import unicodedata
from abc import ABC, abstractmethod
from typing import List

from num2words import num2words


class CipherMachine(ABC):
    @abstractmethod
    def encipher(self, pt: str) -> str:
        pass

    @abstractmethod
    def decipher(self, ct: str) -> str:
        pass

    @abstractmethod
    def set_key(self, key) -> None:
        pass

    @abstractmethod
    def key(self) -> str:
        pass

    # -----------------------------Private-------------------------------- #

    __WORDS_BEFORE_YEAR = [
        "In",
        "During",
        "Since",
        "By",
        "Before",
        "After",
        "Around",
        "From",
        "In the",
        "Throughout",
        "Over",
        "At",
        "Within",
        "For",
        "Until",
        "Following",
        "Before the",
        "After the",
        "By the end of",
        "As of",
        "Throughout the",
        "At the start of",
        "At the time of",
        "From the beginning of",
        "In the year of",
        "In the year",
        "In early",
        "In late",
        "In mid",
        "After the turn of",
        "In the early",
        "In the late",
        "During the course of",
        "Over the course of",
        "At the end of",
        "In advance of",
        "At the beginning of",
        "As early as",
        "As late as",
        "Leading up to",
        "Just before",
        "Just after",
        "In the aftermath of",
        "In light of",
        "Upon",
        "At the conclusion of",
        "In anticipation of",
        "For the duration of",
        "As a result of",
        "In conjunction with",
        "Toward the end of",
    ]

    __UNITS = {
        # **Distance**
        "m": "meter",  # base unit
        "km": "kilometer",  # k * meter
        "ft": "foot",
        "in": "inch",
        "mi": "mile",
        # **Area**
        "m²": "square meter",
        "ft²": "square foot",
        "in²": "square inch",
        "mi²": "square mile",
        # **Volume**
        "L": "liter",  # base unit
        "ml": "milliliter",  # m * liter
        "cm³": "cubic centimeter",  # cm * cm * cm
        "m³": "cubic meter",
        "bbl": "barrel",
        "cu": "cubic",
        # **Mass / Weight**
        "kg": "kilogram",  # k * gram
        "g": "gram",  # base unit
        "lb": "pound",
        "oz": "ounce",
        # **Time**
        "s": "second",  # base unit
        "min": "minute",
        "h": "hour",
        "d": "day",
        "w": "week",
        "mo": "month",
        "yr": "year",
        # **Energy / Work**
        "J": "joule",  # base unit
        "eV": "electronvolt",
        "N·m": "newton-meter",
        "kWh": "kilowatt hour",  # k * watt * hour
        "W": "watt",  # base unit
        # **Temperature**
        "°C": "degree Celsius",
        "°F": "degree Fahrenheit",
        "K": "kelvin",
        # **Electricity**
        "A": "ampere",  # base unit
        "V": "volt",  # base unit
        "Ω": "ohm",  # base unit
        "C": "coulomb",  # base unit
        "Hz": "hertz",
        "Bq": "becquerel",
        "lm": "lumen",
        "lx": "lux",
        "T": "tesla",
        # **Pressure**
        "Pa": "pascal",  # base unit
        "atm": "atmosphere",
        "kPa": "kilopascal",  # k * pascal
        # **Speed**
        "m/s": "meter per second",
        "km/h": "kilometer per hour",
        "ft/s": "foot per second",
        "mph": "mile per hour",
        # **Angles**
        "rad": "radian",
        "sr": "steradian",
        # **Amount of Substance**
        "mol": "mole",
        # **Luminous Intensity**
        "cd": "candela",
        # **Radiation**
        "Sv": "sievert",
        "Gy": "gray",
        # **Miscellaneous**
        "/": "per",
        "p": "per",
        "ppm": "part per million",
        "dB": "decibel",
        "B": "byte",
        "lb·ft": "pound-foot",
        "oz·in": "ounce-inch",
        "ft·lb": "foot-pound",
        "Hz·s": "hertz-second",
    }

    __PREFIXES = {
        "k": "kilo",  # 1000
        "M": "mega",  # 1,000,000
        "G": "giga",  # 1,000,000,000
        "T": "tera",  # 1,000,000,000,000
        "m": "milli",  # 0.001
        "µ": "micro",  # 0.000001
        "n": "nano",  # 0.000000001
        "p": "pico",  # 0.000000000001
        "f": "femto",  # 0.000000000000001
        "c": "centi",  # 0.01
        "d": "deci",  # 0.1
    }

    __CURRENCY = {
        "$": "USD",  # United States Dollar (most common)
        "€": "EUR",  # Euro
        "£": "GBP",  # British Pound Sterling
        "¥": "JPY",  # Japanese Yen
        "₣": "CHF",  # Swiss Franc
        "A$": "AUD",  # Australian Dollar
        "C$": "CAD",  # Canadian Dollar
        "₹": "INR",  # Indian Rupee
        "元": "CNY",  # Chinese Yuan
        "₩": "KRW",  # South Korean Won
        "₪": "ILS",  # Israeli New Shekel
        "₺": "TRY",  # Turkish Lira
        "R$": "BRL",  # Brazilian Real
        "฿": "THB",  # Thai Baht
        "₴": "UAH",  # Ukrainian Hryvnia
        "₱": "PHP",  # Philippine Peso
        "د.إ": "AED",  # United Arab Emirates Dirham
        "د.ج": "DZD",  # Algerian Dinar
        "ر.س": "SAR",  # Saudi Riyal
        "₽": "RUB",  # Russian Ruble
        "₳": "ARS",  # Argentine Peso
        "Rp": "IDR",  # Indonesian Rupiah
        "₤": "HUF",  # Hungarian Forint
        "NT$": "TWD",  # Taiwan Dollar
        "₮": "MNT",  # Mongolian Tugrik
        "₿": "BTC",  # Bitcoin
        "Ξ": "ETH",  # Ethereum
        "X₿": "XRP",  # Ripple (prefix to differentiate from Bitcoin)
        "Ł": "LTC",  # Litecoin (prefix to differentiate from Polish Zloty)
    }

    __ORD_SUFFIX = ["st", "nd", "rd", "th"]

    __PUNCTUATION = [
        "Pc",
        "Pd",
        "Pe",
        "Pf",
        "Pi",
        "Po",
        "Ps",
    ]

    __NOT_OTHER = [
        "Cc",
        "Ll",
        "Lu",
        "Nd",
        "Pc",
        "Pd",
        "Pe",
        "Pf",
        "Pi",
        "Po",
        "Ps",
        "Sk",
        "Zs",
    ]

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
            if text_list[i][0].isdecimal():
                before = text_list[i - 1]
                isYear = False
                for phrase in cls.__WORDS_BEFORE_YEAR:
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
                if before[-1] in cls.__CURRENCY:
                    before[-1] = cls.__CURRENCY[before[-1]] + " "
                    text_list[i - 1] = " ".join(before)
                    text_list[i] = num2words(text_list[i])
                elif after is not None and after[0] in cls.__CURRENCY:
                    before[-1] = cls.__CURRENCY[after[0]] + " "
                    text_list[i - 1] = " ".join(before)
                    text_list[i + 1] = " ".join(after[1:])
                    text_list[i] = num2words(text_list[i])
                elif after is not None and after[0][:2] in cls.__ORD_SUFFIX:
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

        Returns:
            str: The cleaned text.
        """
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
                if unicodedata.category(text[i]) not in cls.__NOT_OTHER:
                    text = text.replace(text[i], "")
                i += 1
        elif conv_other:
            i = 0
            while i < len(text):
                if unicodedata.category(text[i]) not in cls.__NOT_OTHER:
                    text = text.replace(text[i], unicodedata.name(text[i]))
                i += 1

        if not punc:
            i = 0
            while i < len(text):
                if unicodedata.category(text[i]) in cls.__PUNCTUATION:
                    text = text.replace(text[i], "")
                i += 1

        if not accent:
            normal = unicodedata.normalize("NFD", text)
            text = "".join(c for c in normal if not unicodedata.combining(c))

        if not space:
            for char in string.whitespace:
                text = text.replace(char, "")

        return text.upper()

    @staticmethod
    def _create_grid(key: str, size=5) -> List[List[str | None]]:
        """Creates a square grid of the specified size with the provided
        key written left to right throughout it. Empty spaces will be filled with the value None.

        Args:
            key (str): The key for the grid.
            size (int, optional): The size of the grid. Defaults to 5.

        Returns:
            List[List[str | None]]: A square grid of the spcified size with the
            key written from left to right inside of it.
        """
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
        """Removes repeated instances of characters from the input.

        Args:
            text (str): The text to remove repeated characters from.

        Returns:
            str: The text with repeated characters removed.
        """
        new_text = ""
        for char in text:
            if char not in new_text:
                new_text += char
        return new_text
