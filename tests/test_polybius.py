import string

import pytest

from enpypher.polybius import Polybius


@pytest.mark.parametrize(
    "init, pt, ct",
    [
        (
            {"key": "key"},
            "thequickbrownfoxjumpsoverthelazydog",
            "4525124251312111154335533423355431513341443552124345251232145513223524",
        ),
        (
            {"key": "KEY"},
            "thequickbrownfoxjumpsoverthelazydog",
            "4525124251312111154335533423355431513341443552124345251232145513223524",
        ),
        (
            {"key": "key"},
            "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG",
            "4525124251312111154335533423355431513341443552124345251232145513223524",
        ),
        (
            {"key": "key"},
            "the quick brown fox jumps over the lazy dog",
            "452512 4251312111 1543355334 233554 3151334144 35521243 452512 32145513 223524",
        ),
        (
            {"key": "key"},
            "the quick brown fox jumps over 3 lazy dogs.",
            "452512 4251312111 1543355334 233554 3151334144 35521243 4525431212 32145513 22352444.",
        ),
        (
            {"key": "key"},
            "1234567890",
            "353412 15313232313534, 455335 25513422431222 143422 452531434513-23355143 33313232313534, 23315212 25513422431222 143422 4431544513-4412521234 4525355144143422, 1231242545 25513422431222 143422 343134124513",
        ),
        (
            {"key": "thequickbrownfoxjumpsoverthelazydog"},
            "plaintext",
            "424551213311133511",
        ),
        (
            {"key": "the quick brown fox jumps over 3 lazy dogs."},
            "plaintext",
            "424551213311133511",
        ),
        (
            {"key": "secret"},
            "thequickbrownfoxjumpsoverthelazydog",
            "1531124445321333221442524124425332453543114251121415311234215554234225",
        ),
        (
            {"key": "Ελλάδα", "alpha": "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"},
            "Καλημέρα",
            "3113122332114213",
        ),
        (
            {"key": "ΜΥΣΤΙΚΟ", "alpha": "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"},
            "Η γρήγορη καφετιά αλεπού πηδά πάνω από το τεμπέλικο σκυλί.",
            "34 25453425224534 21235132141523 234132442212 44343123 44234254 234422 1422 143211443241152122 1321124115.",
        ),
        (
            {"key": "key", "size": 6, "alpha": string.ascii_uppercase},
            "the quick brown fox jumps over 3 lazy dogs.",
            "432412 3644251611 1541344633 223451 2644323542 34451241 4324411212 31145213 21342342.",
        ),
        (
            {
                "key": "key",
                "size": 6,
                "alpha": string.ascii_uppercase + string.digits,
            },
            "the quick brown fox jumps over 3 lazy dogs.",
            "432412 3644251611 1541344633 223451 2644323542 34451241 56 31145213 21342342.",
        ),
    ],
)
def test_encipher(init, pt, ct):
    pb = Polybius(**init)
    assert pb.encipher(pt) == ct


@pytest.mark.parametrize(
    "init, ct, pt",
    [
        (
            {"key": "key"},
            "4525124251312111154335533423355431513341443552124345251232145513223524",
            "thequickbrownfoxiumpsoverthelazydog",
        ),
        (
            {"key": "KEY"},
            "4525124251312111154335533423355431513341443552124345251232145513223524",
            "thequickbrownfoxiumpsoverthelazydog",
        ),
        (
            {"key": "key"},
            "4525124251312111154335533423355431513341443552124345251232145513223524",
            "thequickbrownfoxiumpsoverthelazydog",
        ),
        (
            {"key": "key"},
            "452512 4251312111 1543355334 233554 3151334144 35521243 452512 32145513 223524",
            "the quick brown fox iumps over the lazy dog",
        ),
        (
            {"key": "key"},
            "452512 4251312111 1543355334 233554 3151334144 35521243 4525431212 32145513 22352444.",
            "the quick brown fox iumps over three lazy dogs.",
        ),
        (
            {"key": "key"},
            "353412 15313232313534, 455335 25513422431222 143422 452531434513-23355143 33313232313534, 23315212 25513422431222 143422 4431544513-4412521234 4525355144143422, 1231242545 25513422431222 143422 343134124513",
            "one billion, two hundred and thirty-four million, five hundred and sixty-seven thousand, eight hundred and ninety",
        ),
        (
            {"key": "thequickbrownfoxjumpsoverthelazydog"},
            "424551213311133511",
            "plaintext",
        ),
        (
            {"key": "the quick brown fox jumps over 3 lazy dogs."},
            "424551213311133511",
            "plaintext",
        ),
        (
            {"key": "secret"},
            "1531124445321333221442524124425332453543114251121415311234215554234225",
            "thequickbrownfoxiumpsoverthelazydog",
        ),
        (
            {"key": "Ελλάδα", "alpha": "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"},
            "3113122332114213",
            "καλημερα",
        ),
        (
            {"key": "ΜΥΣΤΙΚΟ", "alpha": "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"},
            "34 25453425224534 21235132141523 234132442212 44343123 44234254 234422 1422 143211443241152122 1321124115.",
            "η γρηγορη καφετια αλεπου πηδα πανω απο το τεμπελικο σκυλι.",
        ),
        (  # Handle uneven digram case.
            {"key": "key"},
            "452512425131211115433553342335543151334144355212434525123214551322352",
            "thequickbrownfoxiumpsoverthelazydo",
        ),
        (
            {"key": "key", "size": 6, "alpha": string.ascii_uppercase},
            "432412 3644251611 1541344633 223451 2644323542 34451241 4324411212 31145213 21342342.",
            "the quick brown fox jumps over three lazy dogs.",
        ),
        (
            {
                "key": "key",
                "size": 6,
                "alpha": string.ascii_uppercase + string.digits,
            },
            "432412 3644251611 1541344633 223451 2644323542 34451241 56 31145213 21342342.",
            "the quick brown fox jumps over 3 lazy dogs.",
        ),
    ],
)
def test_decipher(init, ct, pt):
    pb = Polybius(**init)
    assert pb.decipher(ct) == pt


@pytest.mark.parametrize(
    "init, exp_key",
    [
        ({"key": "key"}, "key"),
        ({"key": "KEY"}, "KEY"),
        (
            {"key": "ΜΥΣΤΙΚΟ", "alpha": "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"},
            "ΜΥΣΤΙΚΟ",
        ),
    ],
)
def test_key(init, exp_key):
    pb = Polybius(**init)
    assert pb.key() == exp_key


@pytest.mark.parametrize(
    "init, exp_alpha",
    [
        ({"key": "key"}, "ABCDEFGHIKLMNOPQRSTUVWXYZ"),
        (
            {"key": "ΜΥΣΤΙΚΟ", "alpha": "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"},
            "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ",
        ),
    ],
)
def test_alphabet(init, exp_alpha):
    pb = Polybius(**init)
    assert pb.alphabet() == exp_alpha
