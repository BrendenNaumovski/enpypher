import pytest

from enpypher.autokey import Autokey


@pytest.mark.parametrize(
    "init, pt, ct",
    [
        (
            ["key"],
            "thequickbrownfoxjumpsoverthelazydog",
            "DLCJBMSEJTYXETKKOIJYMAKWFOLVEHDJDNE",
        ),
        (
            ["KEY"],
            "thequickbrownfoxjumpsoverthelazydog",
            "DLCJBMSEJTYXETKKOIJYMAKWFOLVEHDJDNE",
        ),
        (
            ["key"],
            "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG",
            "DLCJBMSEJTYXETKKOIJYMAKWFOLVEHDJDNE",
        ),
        (
            ["key"],
            "the quick brown fox jumps over the lazy dog",
            "DLC JBMSE JTYXE TKK OIJYM AKWF OLV EHDJ DNE",
        ),
        (
            ["key"],
            "the quick brown fox jumps over 3 lazy dogs.",
            "DLC JBMSE JTYXE TKK OIJYM AKWF 3 GEQJ DNEV.",
        ),
        (
            ["key"],
            "1234567890",
            "1234567890",
        ),
        (
            ["thequickbrownfoxjumpsoverthelazydog"],
            "plaintext",
            "ISEYHBGHU",
        ),
        (
            ["the quick brown fox jumps over 3 lazy dogs."],
            "plaintext",
            "ISEYHBGHU",
        ),
        (
            ["secret"],
            "thequickbrownfoxjumpsoverthelazydog",
            "LLGHYBVRFHIEPPPOXQZUGLEYDIZSGEQRKSR",
        ),
        (
            ["Ελλάδα", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "Καλημέρα",
            "ΞΛΦΗΟΕΒΑ",
        ),
        (
            ["ΜΥΣΤΙΚΟ", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "Η γρήγορη καφετιά αλεπού πηδά πάνω από το τεμπέλικο σκυλί.",
            "Σ ΧΚΑΛΩΗΝ ΜΡΓΗΙΑΗ ΚΛΑΥΙΔ ΠΗΞΕ ΗΟΘΟ ΗΤΟ ΚΟ ΗΔΜΗΤΕΨΔΤ ΕΑΩΦΡ.",
        ),
    ],
)
def test_encipher(init, pt, ct):
    a = Autokey(*init)
    assert a.encipher(pt) == ct


@pytest.mark.parametrize(
    "init, ct, pt",
    [
        (
            ["key"],
            "DLCJBMSEJTYXETKKOIJYMAKWFOLVEHDJDNE",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            ["KEY"],
            "DLCJBMSEJTYXETKKOIJYMAKWFOLVEHDJDNE",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            ["key"],
            "dlcjbmsejtyxetkkoijymakwfolvehdjdne",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            ["key"],
            "DLC JBMSE JTYXE TKK OIJYM AKWF OLV EHDJ DNE",
            "the quick brown fox jumps over the lazy dog",
        ),
        (
            ["key"],
            "DLC JBMSE JTYXE TKK OIJYM AKWF 3 GEQJ DNEV.",
            "the quick brown fox jumps over 3 lazy dogs.",
        ),
        (
            ["key"],
            "1234567890",
            "1234567890",
        ),
        (
            ["thequickbrownfoxjumpsoverthelazydog"],
            "ISEYHBGHU",
            "plaintext",
        ),
        (
            ["the quick brown fox jumps over 3 lazy dogs."],
            "ISEYHBGHU",
            "plaintext",
        ),
        (
            ["secret"],
            "LLGHYBVRFHIEPPPOXQZUGLEYDIZSGEQRKSR",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            ["Ελλάδα", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "ΞΛΦΗΟΕΒΑ",
            "καλημερα",
        ),
        (
            ["ΜΥΣΤΙΚΟ", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "Σ ΧΚΑΛΩΗΝ ΜΡΓΗΙΑΗ ΚΛΑΥΙΔ ΠΗΞΕ ΗΟΘΟ ΗΤΟ ΚΟ ΗΔΜΗΤΕΨΔΤ ΕΑΩΦΡ.",
            "η γρηγορη καφετια αλεπου πηδα πανω απο το τεμπελικο σκυλι.",
        ),
    ],
)
def test_decipher(init, ct, pt):
    a = Autokey(*init)
    assert a.decipher(ct) == pt
