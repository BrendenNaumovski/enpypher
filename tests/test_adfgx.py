import pytest

from enpypher.adfgx import ADFGX


@pytest.mark.parametrize(
    "init, pt, ct",
    [
        (
            {"grid_key": "key", "trans_key": "secret"},
            "thequickbrownfoxjumpsoverthelazydog",
            "DXAFDFGXGFADXDAFGGFXFDXXAFAXFXGADADXAAXFAADXDFGGGDGFXFFGAXFDAXFXAGDXGD",
        ),
        (
            {"grid_key": "KEY", "trans_key": "SECRET"},
            "thequickbrownfoxjumpsoverthelazydog",
            "DXAFDFGXGFADXDAFGGFXFDXXAFAXFXGADADXAAXFAADXDFGGGDGFXFFGAXFDAXFXAGDXGD",
        ),
        (
            {"grid_key": "key", "trans_key": "secret"},
            "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG",
            "DXAFDFGXGFADXDAFGGFXFDXXAFAXFXGADADXAAXFAADXDFGGGDGFXFFGAXFDAXFXAGDXGD",
        ),
        (
            {"grid_key": "key", "trans_key": "secret"},
            "the quick brown fox jumps over the lazy dog",
            "DDAGFXXGDG XFXGDXFFAAX DXDAAAF GF DDDFDXXAFGXAGAXFAXG AAXFFGXFAGDDF XD FFGXA G",
        ),
        (
            {"grid_key": "key", "trans_key": "secret"},
            "the quick brown fox jumps over 3 lazy dogs.",
            "DDAGFXXGDGADFDXGDXFFAAX FFAXAAAF GF DDAGDGXXAFGXAGAXDA GG AAXFFGXFG XF.DF XD FFGXDXDG",
        ),
        (
            {"grid_key": "secret", "trans_key": "key"},
            "thequickbrownfoxjumpsoverthelazydog",
            "XAGFFDGXAGFGXADAGFDDXDDAAGXAFADGGXDFFGAAXAGXGGXFDGDFDGDDDFXGAXDAAFAXFD",
        ),
        (
            {
                "grid_key": "thisisakeylongerthanthept",
                "trans_key": "thequickbrownfoxjumpsoverthelazydog",
            },
            "plaintext",
            "FADDGXAFDAXGAFAAAG",
        ),
        (
            {
                "grid_key": "this is a key longer than the pt.",
                "trans_key": "the quick brown fox jumps over the lazy dog.",
            },
            "plaintext",
            "FADDGXAFDAXGAFAAAG",
        ),
        (
            {
                "grid_key": "κλειδί",
                "trans_key": "Ελλάδα",
                "alpha": "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ",
            },
            "Καλημέρα",
            "ADADFAAADGAXDDFD",
        ),
        (
            {
                "grid_key": "ΚΛΕΙΔΙ",
                "trans_key": "ΜΥΣΤΙΚΟ",
                "alpha": "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ",
            },
            "Η γρήγορη καφετιά αλεπού πηδά πάνω από το τεμπέλικο σκυλί.",
            "FFAF GGAFAXDAGDGXAGDAA XF GGFADDDAAAXXA  GAAA.DGDGAFDGGXGAAAG DXADAXXAAGFAXXDF AAF DFGFFD AXXDXGDGADDGAFFG",
        ),
    ],
)
def test_encipher(init, pt, ct):
    a = ADFGX(**init)
    assert a.encipher(pt) == ct


@pytest.mark.parametrize(
    "init, ct, pt",
    [
        (
            {"grid_key": "key", "trans_key": "secret"},
            "DXAFDFGXGFADXDAFGGFXFDXXAFAXFXGADADXAAXFAADXDFGGGDGFXFFGAXFDAXFXAGDXGD",
            "thequickbrownfoxiumpsoverthelazydog",
        ),
        (
            {"grid_key": "KEY", "trans_key": "SECRET"},
            "DXAFDFGXGFADXDAFGGFXFDXXAFAXFXGADADXAAXFAADXDFGGGDGFXFFGAXFDAXFXAGDXGD",
            "thequickbrownfoxiumpsoverthelazydog",
        ),
        (
            {"grid_key": "key", "trans_key": "secret"},
            "dxafdfgxgfadxdafggfxfdxxafaxfxgadadxaaxfaadxdfgggdgfxffgaxfdaxfxagdxgd",
            "thequickbrownfoxiumpsoverthelazydog",
        ),
        (
            {"grid_key": "key", "trans_key": "secret"},
            "DDAGFXXGDG XFXGDXFFAAX DXDAAAF GF DDDFDXXAFGXAGAXFAXG AAXFFGXFAGDDF XD FFGXA G",
            "the quick brown fox iumps over the lazy dog",
        ),
        (
            {"grid_key": "key", "trans_key": "secret"},
            "DDAGFXXGDGADFDXGDXFFAAX FFAXAAAF GF DDAGDGXXAFGXAGAXDA GG AAXFFGXFG XF.DF XD FFGXDXDG",
            "the quick brown fox iumps over three lazy dogs.",
        ),
        (
            {"grid_key": "secret", "trans_key": "key"},
            "XAGFFDGXAGFGXADAGFDDXDDAAGXAFADGGXDFFGAAXAGXGGXFDGDFDGDDDFXGAXDAAFAXFD",
            "thequickbrownfoxiumpsoverthelazydog",
        ),
        (
            {
                "grid_key": "thisisakeylongerthanthept",
                "trans_key": "thequickbrownfoxjumpsoverthelazydog",
            },
            "FADDGXAFDAXGAFAAAG",
            "plaintext",
        ),
        (
            {
                "grid_key": "this is a key longer than the pt.",
                "trans_key": "the quick brown fox jumps over the lazy dog.",
            },
            "FADDGXAFDAXGAFAAAG",
            "plaintext",
        ),
        (
            {
                "grid_key": "κλειδί",
                "trans_key": "Ελλάδα",
                "alpha": "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ",
            },
            "ADADFAAADGAXDDFD",
            "καλημερα",
        ),
        (
            {
                "grid_key": "ΚΛΕΙΔΙ",
                "trans_key": "ΜΥΣΤΙΚΟ",
                "alpha": "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ",
            },
            "FFAF GGAFAXDAGDGXAGDAA XF GGFADDDAAAXXA  GAAA.DGDGAFDGGXGAAAG DXADAXXAAGFAXXDF AAF DFGFFD AXXDXGDGADDGAFFG",
            "η γρηγορη καφετια αλεπου πηδα πανω απο το τεμπελικο σκυλι.",
        ),
    ],
)
def test_decipher(init, ct, pt):
    a = ADFGX(**init)
    assert a.decipher(ct) == pt


@pytest.mark.parametrize(
    "init, exp_key",
    [
        ({"grid_key": "key", "trans_key": "secret"}, ("key", "secret")),
        ({"grid_key": "KEY", "trans_key": "SECRET"}, ("KEY", "SECRET")),
        (
            {
                "grid_key": "ΚΛΕΙΔΙ",
                "trans_key": "ΜΥΣΤΙΚΟ",
                "alpha": "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ",
            },
            ("ΚΛΕΙΔΙ", "ΜΥΣΤΙΚΟ"),
        ),
    ],
)
def test_key(init, exp_key):
    a = ADFGX(**init)
    assert a.key() == exp_key


@pytest.mark.parametrize(
    "init, exp_alpha",
    [
        (
            {"grid_key": "key", "trans_key": "secret"},
            "ABCDEFGHIKLMNOPQRSTUVWXYZ",
        ),
        (
            {
                "grid_key": "ΚΛΕΙΔΙ",
                "trans_key": "ΜΥΣΤΙΚΟ",
                "alpha": "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ",
            },
            "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ",
        ),
    ],
)
def test_alphabet(init, exp_alpha):
    a = ADFGX(**init)
    assert a.alphabet() == exp_alpha
