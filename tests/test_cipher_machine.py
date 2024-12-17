import pytest

from enpypher.cipher_machine import CipherMachine


@pytest.mark.parametrize(
    "text, exp_text, space, punc, accent, num, conv_num, conv_units, other, conv_other",
    [
        ("a", "A", False, False, False, False, False, False, False, False),
        ("abc", "ABC", False, False, False, False, False, False, False, False),
        (
            "a b\tc\nd.e?f:g;hi(j)k!l2,m&n$oPQRSTŨVWXYZ",
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
        ),
        (
            "a b\tc\nd.e?f:g;hi(j)k!l2,m&n$oPQRSTŨVWXYZ",
            "A B\tC\nDEFGHIJKLMNOPQRSTUVWXYZ",
            True,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
        ),
        (
            "a b\tc\nd.e?f:g;hi(j)k!l2,m&n$oPQRSTŨVWXYZ",
            "ABCD.E?F:G;HI(J)K!L,M&NOPQRSTUVWXYZ",
            False,
            True,
            False,
            False,
            False,
            False,
            False,
            False,
        ),
        (
            "a b\tc\nd.e?f:g;hi(j)k!l2,m&n$oPQRSTŨVWXYZ",
            "ABCDEFGHIJKLMNOPQRSTŨVWXYZ",
            False,
            False,
            True,
            False,
            False,
            False,
            False,
            False,
        ),
        (
            "a b\tc\nd.e?f:g;hi(j)k!l2,m&n$oPQRSTŨVWXYZ",
            "ABCDEFGHIJKL2MNOPQRSTUVWXYZ",
            False,
            False,
            False,
            True,
            False,
            False,
            False,
            False,
        ),
        (
            "a b\tc\nd.e?f:g;hi(j)k!l2,m&n$oPQRSTŨVWXYZ",
            "ABCDEFGHIJKLTWOMNOPQRSTUVWXYZ",
            False,
            False,
            False,
            True,
            True,
            False,
            False,
            False,
        ),
        (
            "a b\tc\nd.e?f:g;hi(j)k!l2k/hr,m&n$oPQRSTŨVWXYZ",
            "ABCDEFGHIJKLKILOMETERSPERHOURMNOPQRSTUVWXYZ",
            False,
            False,
            False,
            False,
            False,
            True,
            False,
            False,
        ),
        (
            "a b\tc\nd.e?f:g;hi(j)k!l2,m&n$oPQRSTŨVWXYZ",
            "ABCDEFGHIJKLMN$OPQRSTUVWXYZ",
            False,
            False,
            False,
            False,
            False,
            False,
            True,
            False,
        ),
        (
            "a b\tc\nd.e?f:g;hi(j)k!l2,m&n$oPQRSTŨVWXYZ",
            "ABCDEFGHIJKLMNDOLLARSIGNOPQRSTUVWXYZ",
            False,
            False,
            False,
            False,
            False,
            False,
            True,
            True,
        ),
    ],
)
def test__clean_input(
    text,
    exp_text,
    space,
    punc,
    accent,
    num,
    conv_num,
    conv_units,
    other,
    conv_other,
):
    assert (
        CipherMachine._clean_input(
            text,
            space,
            punc,
            accent,
            num,
            conv_num,
            conv_units,
            other,
            conv_other,
        )
        == exp_text
    )


@pytest.mark.parametrize(
    "key, size, exp_grid",
    [
        (
            "a",
            5,
            [
                ["a", None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None],
            ],
        ),
        (
            "abc",
            5,
            [
                ["a", "b", "c", None, None],
                [None, None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None],
            ],
        ),
        (
            "thequickbrownfxjmpsvlazyd",  # the quick brown fox jumps over the lazy dog
            5,
            [
                ["t", "h", "e", "q", "u"],
                ["i", "c", "k", "b", "r"],
                ["o", "w", "n", "f", "x"],
                ["j", "m", "p", "s", "v"],
                ["l", "a", "z", "y", "d"],
            ],
        ),
        (
            "thequickbrownfxjmpsvlazydg",  # the quick brown fox jumps over the lazy dog
            5,
            [
                ["t", "h", "e", "q", "u"],
                ["i", "c", "k", "b", "r"],
                ["o", "w", "n", "f", "x"],
                ["j", "m", "p", "s", "v"],
                ["l", "a", "z", "y", "d"],
            ],
        ),
        (
            "a",
            3,
            [
                ["a", None, None],
                [None, None, None],
                [None, None, None],
            ],
        ),
        (
            "abc",
            3,
            [
                ["a", "b", "c"],
                [None, None, None],
                [None, None, None],
            ],
        ),
        (
            "niecharts",  # nine characters
            3,
            [
                ["n", "i", "e"],
                ["c", "h", "a"],
                ["r", "t", "s"],
            ],
        ),
        (
            "a",
            6,
            [
                ["a", None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
            ],
        ),
        (
            "abcdefghijklmnopqrstuvwxyz0123456789",
            6,
            [
                ["a", "b", "c", "d", "e", "f"],
                ["g", "h", "i", "j", "k", "l"],
                ["m", "n", "o", "p", "q", "r"],
                ["s", "t", "u", "v", "w", "x"],
                ["y", "z", "0", "1", "2", "3"],
                ["4", "5", "6", "7", "8", "9"],
            ],
        ),
    ],
)
def test__create_grid(key, size, exp_grid):
    assert CipherMachine._create_grid(key, size) == exp_grid


@pytest.mark.parametrize(
    "text, exp_text",
    [
        ("a", "a"),
        ("abc", "abc"),
        ("aa", "a"),
        ("aabc", "abc"),
        ("steel", "stel"),
        ("assassinate", "asinte"),
    ],
)
def test__rm_dup(text, exp_text):
    assert CipherMachine._rm_dup(text) == exp_text
