import pytest

from enpypher.polybius import Polybius


@pytest.mark.parametrize(
    "init, pt, ct",
    [
        (
            ["key"],
            "thequickbrownfoxjumpsoverthelazydog",
            "4525124251312111154335533423355431513341443552124345251232145513223524",
        ),
        (
            ["KEY"],
            "thequickbrownfoxjumpsoverthelazydog",
            "4525124251312111154335533423355431513341443552124345251232145513223524",
        ),
        (
            ["key"],
            "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG",
            "4525124251312111154335533423355431513341443552124345251232145513223524",
        ),
        (
            ["key"],
            "the quick brown fox jumps over the lazy dog",
            "452512 4251312111 1543355334 233554 3151334144 35521243 452512 32145513 223524",
        ),
        (
            ["key"],
            "the quick brown fox jumps over 3 lazy dogs.",
            "452512 4251312111 1543355334 233554 3151334144 35521243 4525431212 32145513 22352444.",
        ),
        (
            ["key"],
            "1234567890",
            "353412 15313232313534, 455335 25513422431222 143422 452531434513-23355143 33313232313534, 23315212 25513422431222 143422 4431544513-4412521234 4525355144143422, 1231242545 25513422431222 143422 343134124513",
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
            "34 25453425224534 21235132141523 234132442212 44343123 44234254 234422 1422 143211443241152122 1321124115.",
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
            "4525124251312111154335533423355431513341443552124345251232145513223524",
            "thequickbrownfoxiumpsoverthelazydog",
        ),
        (
            ["KEY"],
            "4525124251312111154335533423355431513341443552124345251232145513223524",
            "thequickbrownfoxiumpsoverthelazydog",
        ),
        (
            ["key"],
            "4525124251312111154335533423355431513341443552124345251232145513223524",
            "thequickbrownfoxiumpsoverthelazydog",
        ),
        (
            ["key"],
            "452512 4251312111 1543355334 233554 3151334144 35521243 452512 32145513 223524",
            "the quick brown fox iumps over the lazy dog",
        ),
        (
            ["key"],
            "452512 4251312111 1543355334 233554 3151334144 35521243 4525431212 32145513 22352444.",
            "the quick brown fox iumps over three lazy dogs.",
        ),
        (
            ["key"],
            "353412 15313232313534, 455335 25513422431222 143422 452531434513-23355143 33313232313534, 23315212 25513422431222 143422 4431544513-4412521234 4525355144143422, 1231242545 25513422431222 143422 343134124513",
            "one billion, two hundred and thirty-four million, five hundred and sixty-seven thousand, eight hundred and ninety",
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
            "thequickbrownfoxiumpsoverthelazydog",
        ),
        (
            ["Ελλάδα", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "3113122332114213",
            "καλημερα",
        ),
        (
            ["ΜΥΣΤΙΚΟ", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "34 25453425224534 21235132141523 234132442212 44343123 44234254 234422 1422 143211443241152122 1321124115.",
            "η γρηγορη καφετια αλεπου πηδα πανω απο το τεμπελικο σκυλι.",
        ),
        (  # Handle uneven digram case.
            ["key"],
            "452512425131211115433553342335543151334144355212434525123214551322352",
            "thequickbrownfoxiumpsoverthelazydo",
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
        (["key"], "ABCDEFGHIKLMNOPQRSTUVWXYZ"),
        (
            ["ΜΥΣΤΙΚΟ", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"],
            "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ♠",
        ),
    ],
)
def test_alphabet(init, exp_alpha):
    pb = Polybius(*init)
    assert pb.alphabet() == exp_alpha
