import pytest

from enpypher.railfence import Railfence


@pytest.mark.parametrize(
    "init, pt, ct",
    [
        (
            [3],
            "thequickbrownfoxjumpsoverthelazydog",
            "TUBNJSRLDHQIKRWFXUPOETEAYOECOOMVHZG",
        ),
        (
            [3],
            "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG",
            "TUBNJSRLDHQIKRWFXUPOETEAYOECOOMVHZG",
        ),
        (
            [3],
            "the quick brown fox jumps over the lazy dog",
            "TQKOFJSEHADH UC RW O UP VRTELZ OEIBNXMO  YG",
        ),
        (
            [3],
            "the quick brown fox jumps over 3 lazy dogs.",
            "TQKOFJSE YGH UC RW O UP VR3LZ OSEIBNXMO AD.",
        ),
        (
            [3],
            "1234567890",
            "1592468037",
        ),
        (
            [5],
            "thequickbrownfoxjumpsoverthelazydog",
            "TBJRDHKRXUETYOECOOMVHZGQIWFPOEAUNSL",
        ),
        (
            [3, "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "Καλημέρα",
            "ΚΜΑΗΈΑΛΡ",
        ),
        (
            [5, "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "Η γρήγορη καφετιά αλεπού πηδά πάνω από το τεμπέλικο σκυλί.",
            "ΗΗΆ ΝΟΙΊ Ρ Ι ΎΠΆΩΤ ΛΚΛ.ΓΟΚΤΑΟΗΠ  ΤΈΟΥΡΓΑΕΛΠΔ ΑΌΕΠ ΚΉΦΕΆΠΜΣ",
        ),
    ],
)
def test_encipher(init, pt, ct):
    r = Railfence(*init)
    assert r.encipher(pt) == ct


@pytest.mark.parametrize(
    "init, ct, pt",
    [
        (
            [3],
            "TUBNJSRLDHQIKRWFXUPOETEAYOECOOMVHZG",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            [3],
            "tubnjsrldhqikrwfxupoeteayoecoomvhzg",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            [3],
            "TQKOFJSEHADH UC RW O UP VRTELZ OEIBNXMO  YG",
            "the quick brown fox jumps over the lazy dog",
        ),
        (
            [3],
            "TQKOFJSE YGH UC RW O UP VR3LZ OSEIBNXMO AD.",
            "the quick brown fox jumps over 3 lazy dogs.",
        ),
        (
            [3],
            "1592468037",
            "1234567890",
        ),
        (
            [5],
            "TBJRDHKRXUETYOECOOMVHZGQIWFPOEAUNSL",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            [3, "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "ΚΜΑΗΈΑΛΡ",
            "καλημέρα",
        ),
        (
            [5, "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "ΗΗΆ ΝΟΙΊ Ρ Ι ΎΠΆΩΤ ΛΚΛ.ΓΟΚΤΑΟΗΠ  ΤΈΟΥΡΓΑΕΛΠΔ ΑΌΕΠ ΚΉΦΕΆΠΜΣ",
            "η γρήγορη καφετιά αλεπού πηδά πάνω από το τεμπέλικο σκυλί.",
        ),
    ],
)
def test_decipher(init, ct, pt):
    r = Railfence(*init)
    assert r.decipher(ct) == pt


@pytest.mark.parametrize(
    "init, exp_key",
    [
        ([3], 3),
        ([5], 5),
        (
            [6, "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            6,
        ),
    ],
)
def test_key(init, exp_key):
    r = Railfence(*init)
    assert r.key() == exp_key


@pytest.mark.parametrize(
    "init, exp_alpha",
    [
        ([3], "ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
        (
            [3, "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ",
        ),
    ],
)
def test_alphabet(init, exp_alpha):
    r = Railfence(*init)
    assert r.alphabet() == exp_alpha
