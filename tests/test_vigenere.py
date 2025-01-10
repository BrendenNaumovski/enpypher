import pytest

from enpypher.vigenere import Vigenere


@pytest.mark.parametrize(
    "init, pt, ct",
    [
        (
            ["key"],
            "thequickbrownfoxjumpsoverthelazydog",
            "DLCAYGMOZBSUXJMHNSWTQYZCBXFOPYJCBYK",
        ),
        (
            ["KEY"],
            "thequickbrownfoxjumpsoverthelazydog",
            "DLCAYGMOZBSUXJMHNSWTQYZCBXFOPYJCBYK",
        ),
        (
            ["key"],
            "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG",
            "DLCAYGMOZBSUXJMHNSWTQYZCBXFOPYJCBYK",
        ),
        (
            ["key"],
            "the quick brown fox jumps over the lazy dog",
            "DLC AYGMO ZBSUX JMH NSWTQ YZCB XFO PYJC BYK",
        ),
        (
            ["key"],
            "the quick brown fox jumps over 3 lazy dogs.",
            "DLC AYGMO ZBSUX JMH NSWTQ YZCB 3 PYJC BYKQ.",
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
            "LLGHYBUODISPFJQONNETUFZXJXJVPTRCFFK",
        ),
        (
            ["Ελλάδα", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "Καλημέρα",
            "ΞΛΦΗΟΕΦΛ",
        ),
        (
            ["ΜΥΣΤΙΚΟ", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "Η γρήγορη καφετιά αλεπού πηδά πάνω από το τεμπέλικο σκυλί.",
            "Σ ΧΚΑΛΩΗΣ ΕΣΟΝΔΨΜ ΥΔΨΩΩΚ ΓΒΦΤ ΩΚΓΛ ΥΙΙ ΓΩ ΙΠΗΙΨΤΣΩΒ ΝΓΞΤΣ.",
        ),
    ],
)
def test_encipher(init, pt, ct):
    v = Vigenere(*init)
    assert v.encipher(pt) == ct


@pytest.mark.parametrize(
    "init, ct, pt",
    [
        (
            ["key"],
            "DLCAYGMOZBSUXJMHNSWTQYZCBXFOPYJCBYK",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            ["KEY"],
            "DLCAYGMOZBSUXJMHNSWTQYZCBXFOPYJCBYK",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            ["key"],
            "dlcaygmozbsuxjmhnswtqyzcbxfopyjcbyk",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            ["key"],
            "DLC AYGMO ZBSUX JMH NSWTQ YZCB XFO PYJC BYK",
            "the quick brown fox jumps over the lazy dog",
        ),
        (
            ["key"],
            "DLC AYGMO ZBSUX JMH NSWTQ YZCB 3 PYJC BYKQ.",
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
            "LLGHYBUODISPFJQONNETUFZXJXJVPTRCFFK",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            ["Ελλάδα", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "ΞΛΦΗΟΕΦΛ",
            "καλημερα",
        ),
        (
            ["ΜΥΣΤΙΚΟ", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "Σ ΧΚΑΛΩΗΣ ΕΣΟΝΔΨΜ ΥΔΨΩΩΚ ΓΒΦΤ ΩΚΓΛ ΥΙΙ ΓΩ ΙΠΗΙΨΤΣΩΒ ΝΓΞΤΣ.",
            "η γρηγορη καφετια αλεπου πηδα πανω απο το τεμπελικο σκυλι.",
        ),
    ],
)
def test_decipher(init, ct, pt):
    v = Vigenere(*init)
    assert v.decipher(ct) == pt


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
    v = Vigenere(*init)
    assert v.key() == exp_key


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
    v = Vigenere(*init)
    assert v.alphabet() == exp_alpha
