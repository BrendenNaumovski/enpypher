import pytest

from enpypher.polybius import Polybius


@pytest.mark.parametrize(
    "init, pt, ct",
    [
        (
            ["key"],
            "thequickbrownfoxjumpsoverthelazydog",
            "4525124251312111514335533423355431513341443552124345251232145513223524",
        ),
        (
            ["KEY"],
            "thequickbrownfoxjumpsoverthelazydog",
            "4525124251312111514335533423355431513341443552124345251232145513223524",
        ),
        (
            ["key"],
            "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG",
            "4525124251312111514335533423355431513341443552124345251232145513223524",
        ),
        (
            ["key"],
            "the quick brown fox jumps over the lazy dog",
            "452512 4251312111 5143355334 233554 3151334144 35521243 452512 32145513 223524",
        ),
        (
            ["key"],
            "the quick brown fox jumps over 3 lazy dogs.",
            "452512 4251312111 5143355334 233554 3151334144 35521243 4525431212 32145513 22352444.",
        ),
        (
            ["key"],
            "1234567890",
            "35341245533545254312122335514325315212443154441252123412312425453431341255124335",
        ),
        (
            ["thequickbrownfoxjumpsoverthelazydog"],
            "plaintext",
            "424551213311133511",
        ),
        (
            ["the quick brown fox jumps over 3 lazy dogs."],
            "plaintext",
            "424551213311133511",
        ),
        (
            ["secret"],
            "thequickbrownfoxjumpsoverthelazydog",
            "1531124445321333221442524124425332453543114251121415311234215554234225",
        ),
        (
            ["Ελλάδα", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "Καλημέρα",
            "3113122332114213",
        ),
        (
            ["ΜΥΣΤΙΚΟ", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "Η γρήγορη καφετιά αλεπού πηδά πάνω από το τεμπέλικο σκυλί.",
            "34 25453425224534 21235132141523 234132442212 44343123 44234253 234422 1422 143211443241152122 1321124115.",
        ),
    ],
)
def test_encipher(init, pt, ct):
    pb = Polybius(*init)
    assert pb.encipher(pt) == ct


@pytest.mark.parametrize(
    "init, ct, pt",
    [
        (
            ["key"],
            "4525124251312111514335533423355431513341443552124345251232145513223524",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            ["KEY"],
            "4525124251312111514335533423355431513341443552124345251232145513223524",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            ["key"],
            "4525124251312111514335533423355431513341443552124345251232145513223524",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            ["key"],
            "SFB PTGYI EQNVM CNW HTLOR NUBQ SFB JKZX AND",
            "452512 4251312111 5143355334 233554 3151334144 35521243 452512 32145513 223524",
        ),
        (
            ["key"],
            "SFB PTGYI EQNVM CNW HTLOR NUBQ 3 JKZX ANDR.",
            "452512 4251312111 5143355334 233554 3151334144 35521243 4525431212 32145513 22352444.",
        ),
        (
            ["key"],
            "35341245533545254312122335514325315212443154441252123412312425453431341255124335",
            "onetwothreefourfivesixseveneightninezero",
        ),
        (
            ["thequickbrownfoxjumpsoverthelazydog"],
            "424551213311133511",
            "plaintext",
        ),
        (
            ["the quick brown fox jumps over 3 lazy dogs."],
            "424551213311133511",
            "plaintext",
        ),
        (
            ["secret"],
            "1531124445321333221442524124425332453543114251121415311234215554234225",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            ["Ελλάδα", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "3113122332114213",
            "καλημερα",
        ),
        (
            ["ΜΥΣΤΙΚΟ", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "34 25453425224534 21235132141523 234132442212 44343123 44234253 234422 1422 143211443241152122 1321124115.",
            "η γρηγορη καφετια αλεπου πηδα πανω απο το τεμπελικο σκυλι.",
        ),
    ],
)
def test_decipher(init, ct, pt):
    pb = Polybius(*init)
    assert pb.decipher(ct) == pt


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
    pb = Polybius(*init)
    assert pb.key() == exp_key


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
    pb = Polybius(*init)
    assert pb.alphabet() == exp_alpha
