import pytest

from enpypher.shift import Shift


@pytest.mark.parametrize(
    "init, pt, ct",
    [
        (
            [0],
            "thequickbrownfoxjumpsoverthelazydog",
            "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG",
        ),
        (
            [1],
            "thequickbrownfoxjumpsoverthelazydog",
            "UIFRVJDLCSPXOGPYKVNQTPWFSUIFMBAZEPH",
        ),
        (
            [3],
            "thequickbrownfoxjumpsoverthelazydog",
            "WKHTXLFNEURZQIRAMXPSVRYHUWKHODCBGRJ",
        ),
        (
            [26],
            "thequickbrownfoxjumpsoverthelazydog",
            "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG",
        ),
        (
            [27],
            "thequickbrownfoxjumpsoverthelazydog",
            "UIFRVJDLCSPXOGPYKVNQTPWFSUIFMBAZEPH",
        ),
        (
            [-3],
            "thequickbrownfoxjumpsoverthelazydog",
            "QEBNRFZHYOLTKCLUGRJMPLSBOQEBIXWVALD",
        ),
        (
            [3],
            "the quick brown fox jumps over the lazy dog",
            "WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ",
        ),
        (
            [3],
            "the quick brown fox jumps over 3 lazy dogs.",
            "WKH TXLFN EURZQ IRA MXPSV RYHU 3 ODCB GRJV.",
        ),
        (
            [3],
            "1234567890",
            "1234567890",
        ),
        (
            [3, "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "Καλημέρα",
            "ΝΔΞΚΟΘΥΔ",
        ),
        (
            [3, "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "Η γρήγορη καφετιά αλεπού πηδά πάνω από το τεμπέλικο σκυλί.",
            "Κ ΖΥΚΖΣΥΚ ΝΔΩΘΧΜΔ ΔΞΘΤΣΨ ΤΚΗΔ ΤΔΠΓ ΔΤΣ ΧΣ ΧΘΟΤΘΞΜΝΣ ΦΝΨΞΜ.",
        ),
    ],
)
def test_encipher(init, pt, ct):
    s = Shift(*init)
    assert s.encipher(pt) == ct


@pytest.mark.parametrize(
    "init, ct, pt",
    [
        (
            [0],
            "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            [1],
            "UIFRVJDLCSPXOGPYKVNQTPWFSUIFMBAZEPH",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            [3],
            "WKHTXLFNEURZQIRAMXPSVRYHUWKHODCBGRJ",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            [26],
            "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            [27],
            "UIFRVJDLCSPXOGPYKVNQTPWFSUIFMBAZEPH",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            [-3],
            "QEBNRFZHYOLTKCLUGRJMPLSBOQEBIXWVALD",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            [3],
            "WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ",
            "the quick brown fox jumps over the lazy dog",
        ),
        (
            [3],
            "WKH TXLFN EURZQ IRA MXPSV RYHU 3 ODCB GRJV.",
            "the quick brown fox jumps over 3 lazy dogs.",
        ),
        (
            [3],
            "1234567890",
            "1234567890",
        ),
        (
            [3, "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "ΝΔΞΚΟΘΥΔ",
            "καλημερα",
        ),
        (
            [3, "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "Κ ΖΥΚΖΣΥΚ ΝΔΩΘΧΜΔ ΔΞΘΤΣΨ ΤΚΗΔ ΤΔΠΓ ΔΤΣ ΧΣ ΧΘΟΤΘΞΜΝΣ ΦΝΨΞΜ.",
            "η γρηγορη καφετια αλεπου πηδα πανω απο το τεμπελικο σκυλι.",
        ),
    ],
)
def test_decipher(init, ct, pt):
    s = Shift(*init)
    assert s.decipher(ct) == pt


@pytest.mark.parametrize(
    "init, exp_key",
    [
        ([0], ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 0)),
        ([1], ("BCDEFGHIJKLMNOPQRSTUVWXYZA", 1)),
        ([3], ("DEFGHIJKLMNOPQRSTUVWXYZABC", 3)),
        ([26], ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 26)),
        ([27], ("BCDEFGHIJKLMNOPQRSTUVWXYZA", 27)),
        ([-3], ("XYZABCDEFGHIJKLMNOPQRSTUVW", -3)),
    ],
)
def test_key(init, exp_key):
    s = Shift(*init)
    assert s.key() == exp_key


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
    s = Shift(*init)
    assert s.alphabet() == exp_alpha
