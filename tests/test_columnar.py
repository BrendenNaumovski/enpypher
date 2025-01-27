import pytest

from enpypher.columnar import Columnar


@pytest.mark.parametrize(
    "init, pt, ct",
    [
        (
            ["key"],
            "thequickbrownfoxjumpsoverthelazydog",
            "HUKOFJPVTLYGTQCRNXMOREZOEIBWOUSEHAD",
        ),
        (
            ["KEY"],
            "thequickbrownfoxjumpsoverthelazydog",
            "HUKOFJPVTLYGTQCRNXMOREZOEIBWOUSEHAD",
        ),
        (
            ["key"],
            "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG",
            "HUKOFJPVTLYGTQCRNXMOREZOEIBWOUSEHAD",
        ),
        (
            ["key"],
            "the quick brown fox jumps over the lazy dog",
            "HQCBWF M ET ZDT I O XUSV EA GEUKRNOJPORHLYO",
        ),
        (
            ["key"],
            "the quick brown fox jumps over 3 lazy dogs.",
            "HQCBWF M E3A GT I O XUSV LYO.EUKRNOJPOR ZDS",
        ),
        (
            ["key"],
            "1234567890",
            "2581470369",
        ),
        (
            ["thequickbrownfoxjumpsoverthelazydog"],
            "plaintext",
            "TEALTXIPN",
        ),
        (
            ["the quick brown fox jumps over 3 lazy dogs."],
            "plaintext",
            "TEALTXIPN",
        ),
        (
            ["secret"],
            "thequickbrownfoxjumpsoverthelazydog",
            "EBOSHDHKFPTYUOJVLGQRXOEOTCNMRZIWUEA",
        ),
        (
            ["secret"],
            "the quick brown fox jumps over 3 lazy dogs.",
            "EKNJO DHCW  3 QBFMEAG   UVLOTIOXS Y.UROPRZS",
        ),
        (
            ["Ελλάδα", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "Καλημέρα",
            "ΗΕΜΚΡΑΑΛ",
        ),
        (
            ["ΜΥΣΤΙΚΟ", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "Η γρήγορη καφετιά αλεπού πηδά πάνω από το τεμπέλικο σκυλί.",
            "ΗΑΑΠΝΤΕΚΓΦΛΗΩΟΛΥΗΡΤΠΑΑΤΚΙΟΕΕΔ  ΙΛΓ ΑΥΠΟΜ ΡΚ  Α ΠΣ ΗΙΟ ΠΕΟ.",
        ),
        (  # Case added to test full grid after trouble with ADFGX
            ["secret"],
            "GXDXAD GDXAFADAAA AXGFFXXFFG DFFXXG FAXAFFGAGG FXXDADGF GXDXAD FDAGXXAF DDFXDG",
            "DDAGFXXGDG XFXGDXFFAAX DXDAAAF GF DDDFDXXAFGXAGAXFAXG AAXFFGXFAGDDF XD FFGXA G",
        ),
    ],
)
def test_encipher(init, pt, ct):
    c = Columnar(*init)
    assert c.encipher(pt) == ct


@pytest.mark.parametrize(
    "init, ct, pt",
    [
        (
            ["key"],
            "HUKOFJPVTLYGTQCRNXMOREZOEIBWOUSEHAD",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            ["KEY"],
            "HUKOFJPVTLYGTQCRNXMOREZOEIBWOUSEHAD",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            ["key"],
            "hukofjpvtlygtqcrnxmorezoeibwousehad",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            ["key"],
            "HQCBWF M ET ZDT I O XUSV EA GEUKRNOJPORHLYO",
            "the quick brown fox jumps over the lazy dog",
        ),
        (
            ["key"],
            "HQCBWF M E3A GT I O XUSV LYO.EUKRNOJPOR ZDS",
            "the quick brown fox jumps over 3 lazy dogs.",
        ),
        (
            ["key"],
            "2581470369",
            "1234567890",
        ),
        (
            ["thequickbrownfoxjumpsoverthelazydog"],
            "TEALTXIPN",
            "plaintext",
        ),
        (
            ["the quick brown fox jumps over 3 lazy dogs."],
            "TEALTXIPN",
            "plaintext",
        ),
        (
            ["secret"],
            "EBOSHDHKFPTYUOJVLGQRXOEOTCNMRZIWUEA",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            ["secret"],
            "EKNJO DHCW  3 QBFMEAG   UVLOTIOXS Y.UROPRZS",
            "the quick brown fox jumps over 3 lazy dogs.",
        ),
        (
            ["Ελλάδα", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "ΗΕΜΚΡΑΑΛ",
            "καλημερα",
        ),
        (
            ["ΜΥΣΤΙΚΟ", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "ΗΑΑΠΝΤΕΚΓΦΛΗΩΟΛΥΗΡΤΠΑΑΤΚΙΟΕΕΔ  ΙΛΓ ΑΥΠΟΜ ΡΚ  Α ΠΣ ΗΙΟ ΠΕΟ.",
            "η γρηγορη καφετια αλεπου πηδα πανω απο το τεμπελικο σκυλι.",
        ),
        (  # Case added to test full grid after trouble with ADFGX
            ["secret"],
            "DDAGFXXGDG XFXGDXFFAAX DXDAAAF GF DDDFDXXAFGXAGAXFAXG AAXFFGXFAGDDF XD FFGXA G",
            "gxdxad gdxafadaaa axgffxxffg dffxxg faxaffgagg fxxdadgf gxdxad fdagxxaf ddfxdg",
        ),
    ],
)
def test_decipher(init, ct, pt):
    c = Columnar(*init)
    assert c.decipher(ct) == pt


@pytest.mark.parametrize(
    "init, exp_key",
    [
        (["key"], "key"),
        (["KEY"], "KEY"),
        (["secret"], "secret"),
        (
            ["thequickbrownfoxjumpsoverthelazydog"],
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            ["the quick brown fox jumps over 3 lazy dogs."],
            "the quick brown fox jumps over 3 lazy dogs.",
        ),
        (
            ["ΜΥΣΤΙΚΟ", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "ΜΥΣΤΙΚΟ",
        ),
    ],
)
def test_key(init, exp_key):
    c = Columnar(*init)
    assert c.key() == exp_key


@pytest.mark.parametrize(
    "init, exp_alpha",
    [
        (["key"], "ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
        (
            ["ΜΥΣΤΙΚΟ", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ",
        ),
    ],
)
def test_alphabet(init, exp_alpha):
    c = Columnar(*init)
    assert c.alphabet() == exp_alpha
