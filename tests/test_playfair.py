import pytest

from enpypher.playfair import Playfair


@pytest.mark.parametrize(
    "init, pt, ct",
    [
        (
            ["key"],
            "thequickbrownfoxjumpsoverthelazydog",
            "ZODVKPICYTMZMGNZPKIRTNEDSPDBNEWBHLNA",
        ),
        (
            ["KEY"],
            "thequickbrownfoxjumpsoverthelazydog",
            "ZODVKPICYTMZMGNZPKIRTNEDSPDBNEWBHLNA",
        ),
        (
            ["key"],
            "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG",
            "ZODVKPICYTMZMGNZPKIRTNEDSPDBNEWBHLNA",
        ),
        (
            ["key"],
            "the quick brown fox jumps over the lazy dog",
            "ZOD VKPIC YTMZM GNZ PKIRT NEDS PDB NEWB HLNA",
        ),
        (
            ["key"],
            "the quick brown fox jumps over 3 lazy dogs.",
            "ZOD VKPIC YTMZM GNZ PKIRT NEDQ 3 MBXE FNHX.A",
        ),
        (
            ["key"],
            "1234567890",
            "1234567890",
        ),
        (
            ["thequickbrownfoxjumpsoverthelazydog"],
            "plaintext",
            "SMTOOEUNUO",
        ),
        (
            ["the quick brown fox jumps over 3 lazy dogs."],
            "plaintext",
            "SMTOOEUNUO",
        ),
        (
            ["secret"],
            "thequickbrownfoxjumpsoverthelazydog",
            "SMROOMDPFEWEQAPWMOKUENWSTSISHFVZBPDZ",
        ),
        (
            ["secret"],
            "mybiggestjigsawpuzzleisapictureofstarrynight",
            "LZIODZBTESKWMBAHXOZTYMBOAHOKRSQTBWARSGCYFROHAMCZ",
        ),
        (
            ["Ελλάδα", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "Καλημέρα",
            "ΝΕΑΖΚΛΣΛ",
        ),
        (
            ["ΜΥΣΤΙΚΟ", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "Η γρήγορη καφετιά αλεπού πηδά πάνω από το τεμπέλικο σκυλί.",
            "Θ ΒΠΘΚΑΠΘ ΟΒΧΔΙΜΓ ΨΚΞΗΝΕΟ ΩΠΖΚ ΞΒΠΧ ΒΞΒ ΥΒ ΥΔΥΝΗΡΜΟΑ ΜΑΜΝΓ.Ι",
        ),
    ],
)
def test_encipher(init, pt, ct):
    p = Playfair(*init)
    assert p.encipher(pt) == ct


@pytest.mark.parametrize(
    "init, ct, pt",
    [
        (
            ["key"],
            "ZODVKPICYTMZMGNZPKIRTNEDSPDBNEWBHLNA",
            "thequickbrownfoxiumpsoverthelazydogx",
        ),
        (
            ["KEY"],
            "ZODVKPICYTMZMGNZPKIRTNEDSPDBNEWBHLNA",
            "thequickbrownfoxiumpsoverthelazydogx",
        ),
        (
            ["key"],
            "zodvkpicytmzmgnzpkirtnedspdbnewbhlna",
            "thequickbrownfoxiumpsoverthelazydogx",
        ),
        (
            ["key"],
            "ZOD VKPIC YTMZM GNZ PKIRT NEDS PDB NEWB HLNA",
            "the quick brown fox iumps over the lazy dogx",
        ),
        (
            ["key"],
            "ZOD VKPIC YTMZM GNZ PKIRT NEDQ 3 MBXE FNHX.A",
            "the quick brown fox iumps over 3 lazy dogs.x",
        ),
        (
            ["key"],
            "1234567890",
            "1234567890",
        ),
        (
            ["thequickbrownfoxjumpsoverthelazydog"],
            "SMTOOEUNUO",
            "plaintextx",
        ),
        (
            ["the quick brown fox jumps over 3 lazy dogs."],
            "SMTOOEUNUO",
            "plaintextx",
        ),
        (
            ["secret"],
            "SMROOMDPFEWEQAPWMOKUENWSTSISHFVZBPDZ",
            "thequickbrownfoxiumpsoverthelazydogx",
        ),
        (
            ["secret"],
            "LZIODZBTESKWMBAHXOZTYMBOAHOKRSQTBWARSGCYFROHAMCZ",
            "mybigxgestixigsawpuzzleisapictureofstarxrynightx",
        ),
        (
            ["Ελλάδα", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "ΝΕΑΖΚΛΣΛ",
            "καλημερα",
        ),
        (
            ["ΜΥΣΤΙΚΟ", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "Θ ΒΠΘΚΑΠΘ ΟΒΧΔΙΜΓ ΨΚΞΗΝΕΟ ΩΠΖΚ ΞΒΠΧ ΒΞΒ ΥΒ ΥΔΥΝΗΡΜΟΑ ΜΑΜΝΓ.Ι",
            "η γρηγορη καφετια ♠αλεπου πηδα πανω απο το τεμπελικο σκυλι.♠",
        ),
    ],
)
def test_decipher(init, ct, pt):
    p = Playfair(*init)
    assert p.decipher(ct) == pt


@pytest.mark.parametrize(
    "init, exp_key",
    [
        (["key"], ("key")),
        (["KEY"], ("KEY")),
        (["secret"], ("secret")),
        (
            ["thequickbrownfoxjumpsoverthelazydog"],
            ("thequickbrownfoxjumpsoverthelazydog"),
        ),
        (
            ["the quick brown fox jumps over 3 lazy dogs."],
            ("the quick brown fox jumps over 3 lazy dogs."),
        ),
        (
            ["ΜΥΣΤΙΚΟ", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            ("ΜΥΣΤΙΚΟ"),
        ),
    ],
)
def test_key(init, exp_key):
    p = Playfair(*init)
    assert p.key() == exp_key


@pytest.mark.parametrize(
    "init, exp_alpha",
    [
        (["key"], "ABCDEFGHIKLMNOPQRSTUVWXYZ"),
        (
            ["ΜΥΣΤΙΚΟ", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ♠",
        ),
    ],
)
def test_alphabet(init, exp_alpha):
    p = Playfair(*init)
    assert p.alphabet() == exp_alpha
