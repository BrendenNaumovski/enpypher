import pytest

from enpypher.monoalphabetic import Monoalphabetic


@pytest.mark.parametrize(
    "init, pt, ct",
    [
        (
            ["key"],
            "thequickbrownfoxjumpsoverthelazydog",
            "SFBPTGYIEQNVMCNWHTLORNUBQSFBJKZXAND",
        ),
        (
            ["KEY"],
            "thequickbrownfoxjumpsoverthelazydog",
            "SFBPTGYIEQNVMCNWHTLORNUBQSFBJKZXAND",
        ),
        (
            ["key"],
            "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG",
            "SFBPTGYIEQNVMCNWHTLORNUBQSFBJKZXAND",
        ),
        (
            ["key"],
            "the quick brown fox jumps over the lazy dog",
            "SFB PTGYI EQNVM CNW HTLOR NUBQ SFB JKZX AND",
        ),
        (
            ["key"],
            "the quick brown fox jumps over 3 lazy dogs.",
            "SFB PTGYI EQNVM CNW HTLOR NUBQ 3 JKZX ANDR.",
        ),
        (
            ["key"],
            "1234567890",
            "1234567890",
        ),
        (
            ["thequickbrownfoxjumpsoverthelazydog"],
            "plaintext",
            "JWTBFVUYV",
        ),
        (
            ["the quick brown fox jumps over 3 lazy dogs."],
            "plaintext",
            "JWTBFVUYV",
        ),
        (
            ["secret"],
            "thequickbrownfoxjumpsoverthelazydog",
            "QDTNUFCHEOLWKALXGUJMPLVTOQDTISZYRLB",
        ),
        (
            ["defghijklmnopqrstuvwxyzabc"],
            "thequickbrownfoxjumpsoverthelazydog",
            "WKHTXLFNEURZQIRAMXPSVRYHUWKHODCBGRJ",
        ),
        (
            ["Ελλάδα", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "Καλημέρα",
            "ΙΕΚΖΜΒΡΕ",
        ),
        (
            ["ΜΥΣΤΙΚΟ", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "Η γρήγορη καφετιά αλεπού πηδά πάνω από το τεμπέλικο σκυλί.",
            "Ο ΣΝΟΣΘΝΟ ΓΜΦΙΠΒΜ ΜΔΙΛΘΡ ΛΟΤΜ ΛΜΖΩ ΜΛΘ ΠΘ ΠΙΕΛΙΔΒΓΘ ΞΓΡΔΒ.",
        ),
    ],
)
def test_encipher(init, pt, ct):
    ma = Monoalphabetic(*init)
    assert ma.encipher(pt) == ct


@pytest.mark.parametrize(
    "init, ct, pt",
    [
        (
            ["key"],
            "SFBPTGYIEQNVMCNWHTLORNUBQSFBJKZXAND",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            ["KEY"],
            "SFBPTGYIEQNVMCNWHTLORNUBQSFBJKZXAND",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            ["key"],
            "sfbptgyieqnvmcnwhtlornubqsfbjkzxand",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            ["key"],
            "SFB PTGYI EQNVM CNW HTLOR NUBQ SFB JKZX AND",
            "the quick brown fox jumps over the lazy dog",
        ),
        (
            ["key"],
            "SFB PTGYI EQNVM CNW HTLOR NUBQ 3 JKZX ANDR.",
            "the quick brown fox jumps over 3 lazy dogs.",
        ),
        (
            ["key"],
            "1234567890",
            "1234567890",
        ),
        (
            ["thequickbrownfoxjumpsoverthelazydog"],
            "JWTBFVUYV",
            "plaintext",
        ),
        (
            ["the quick brown fox jumps over 3 lazy dogs."],
            "JWTBFVUYV",
            "plaintext",
        ),
        (
            ["secret"],
            "QDTNUFCHEOLWKALXGUJMPLVTOQDTISZYRLB",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            ["defghijklmnopqrstuvwxyzabc"],
            "WKHTXLFNEURZQIRAMXPSVRYHUWKHODCBGRJ",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            ["Ελλάδα", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "ΙΕΚΖΜΒΡΕ",
            "καλημερα",
        ),
        (
            ["ΜΥΣΤΙΚΟ", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "Ο ΣΝΟΣΘΝΟ ΓΜΦΙΠΒΜ ΜΔΙΛΘΡ ΛΟΤΜ ΛΜΖΩ ΜΛΘ ΠΘ ΠΙΕΛΙΔΒΓΘ ΞΓΡΔΒ.",
            "η γρηγορη καφετια αλεπου πηδα πανω απο το τεμπελικο σκυλι.",
        ),
    ],
)
def test_decipher(init, ct, pt):
    ma = Monoalphabetic(*init)
    assert ma.decipher(ct) == pt


@pytest.mark.parametrize(
    "init, exp_key",
    [
        (["key"], "key"),
        (["KEY"], "KEY"),
        (["secret"], "secret"),
        (["defghijklmnopqrstuvwxyzabc"], "defghijklmnopqrstuvwxyzabc"),
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
    ma = Monoalphabetic(*init)
    assert ma.key() == exp_key


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
    ma = Monoalphabetic(*init)
    assert ma.alphabet() == exp_alpha
