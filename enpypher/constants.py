_WORDS_BEFORE_YEAR = {
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
}

_UNITS = {
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

_PREFIXES = {
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

_CURRENCY = {
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

_ORD_SUFFIX = {"st", "nd", "rd", "th"}

_PUNCTUATION = {
    "Pc",
    "Pd",
    "Pe",
    "Pf",
    "Pi",
    "Po",
    "Ps",
}

_NOT_OTHER = {
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
}
