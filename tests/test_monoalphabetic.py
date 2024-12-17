import pytest

from enpypher.monoalphabetic import Monoalphabetic


@pytest.mark.parametrize(
    "key, pt, ct",
    [
        (
            "key",
            "thequickbrownfoxjumpsoverthelazydog",
            "SFBPTGYIEQNVMCNWHTLORNUBQSFBJKZXAND",
        ),
        (
            "KEY",
            "thequickbrownfoxjumpsoverthelazydog",
            "SFBPTGYIEQNVMCNWHTLORNUBQSFBJKZXAND",
        ),
        (
            "key",
            "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG",
            "SFBPTGYIEQNVMCNWHTLORNUBQSFBJKZXAND",
        ),
        (
            "key",
            "the quick brown fox jumps over the lazy dog",
            "SFB PTGYI EQNVM CNW HTLOR NUBQ SFB JKZX AND",
        ),
        (
            "key",
            "the quick brown fox jumps over 3 lazy dogs.",
            "SFB PTGYI EQNVM CNW HTLOR NUBQ 3 JKZX ANDR.",
        ),
        (
            "thequickbrownfoxjumpsoverthelazydog",
            "plaintext",
            "JWTBFVUYV",
        ),
        (
            "the quick brown fox jumps over 3 lazy dogs.",
            "plaintext",
            "JWTBFVUYV",
        ),
        (
            "secret",
            "thequickbrownfoxjumpsoverthelazydog",
            "QDTNUFCHEOLWKALXGUJMPLVTOQDTISZYRLB",
        ),
        (
            "defghijklmnopqrstuvwxyzabc",
            "thequickbrownfoxjumpsoverthelazydog",
            "WKHTXLFNEURZQIRAMXPSVRYHUWKHODCBGRJ",
        ),
        (
            "key",
            "1234567890",
            "1234567890",
        ),
    ],
)
def test_encipher(key, pt, ct):
    ma = Monoalphabetic(key)
    assert ma.encipher(pt) == ct


@pytest.mark.parametrize(
    "key, ct, pt",
    [
        (
            "key",
            "SFBPTGYIEQNVMCNWHTLORNUBQSFBJKZXAND",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            "KEY",
            "SFBPTGYIEQNVMCNWHTLORNUBQSFBJKZXAND",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            "key",
            "sfbptgyieqnvmcnwhtlornubqsfbjkzxand",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            "key",
            "SFB PTGYI EQNVM CNW HTLOR NUBQ SFB JKZX AND",
            "the quick brown fox jumps over the lazy dog",
        ),
        (
            "key",
            "SFB PTGYI EQNVM CNW HTLOR NUBQ 3 JKZX ANDR.",
            "the quick brown fox jumps over 3 lazy dogs.",
        ),
        (
            "thequickbrownfoxjumpsoverthelazydog",
            "JWTBFVUYV",
            "plaintext",
        ),
        (
            "the quick brown fox jumps over 3 lazy dogs.",
            "JWTBFVUYV",
            "plaintext",
        ),
        (
            "secret",
            "QDTNUFCHEOLWKALXGUJMPLVTOQDTISZYRLB",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            "defghijklmnopqrstuvwxyzabc",
            "WKHTXLFNEURZQIRAMXPSVRYHUWKHODCBGRJ",
            "thequickbrownfoxjumpsoverthelazydog",
        ),
        (
            "key",
            "1234567890",
            "1234567890",
        ),
    ],
)
def test_decipher(key, ct, pt):
    ma = Monoalphabetic(key)
    assert ma.decipher(ct) == pt


@pytest.mark.parametrize(
    "key, exp_key",
    [
        ("key", ("KEYABCDFGHIJLMNOPQRSTUVWXZ", "key")),
        ("KEY", ("KEYABCDFGHIJLMNOPQRSTUVWXZ", "KEY")),
        ("secret", ("SECRTABDFGHIJKLMNOPQUVWXYZ", "secret")),
        (
            "defghijklmnopqrstuvwxyzabc",
            ("DEFGHIJKLMNOPQRSTUVWXYZABC", "defghijklmnopqrstuvwxyzabc"),
        ),
        (
            "thequickbrownfoxjumpsoverthelazydog",
            (
                "THEQUICKBROWNFXJMPSVLAZYDG",
                "thequickbrownfoxjumpsoverthelazydog",
            ),
        ),
        (
            "the quick brown fox jumps over 3 lazy dogs.",
            (
                "THEQUICKBROWNFXJMPSVLAZYDG",
                "the quick brown fox jumps over 3 lazy dogs.",
            ),
        ),
    ],
)
def test_key(key, exp_key):
    ma = Monoalphabetic(key)
    assert ma.key() == exp_key
