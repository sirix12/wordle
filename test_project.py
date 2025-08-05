from WODL import get_word, check, get_n, get_guess
from pytest import raises

def test_get_word():
    assert len(get_word(4)) == 4
    assert len(get_word(9)) == 9
    assert len(get_word(3)) == 3
    assert len(get_word(12)) == 12
    with raises(SystemExit):
        assert get_word(25)
def test_check():
    assert check("KIBLA", "MOUNT") == ['\x1b[5m\x1b[7m\x1b[31mM\x1b[0m', '\x1b[5m\x1b[7m\x1b[31mO\x1b[0m',
                                       '\x1b[5m\x1b[7m\x1b[31mU\x1b[0m', '\x1b[5m\x1b[7m\x1b[31mN\x1b[0m', '\x1b[5m\x1b[7m\x1b[31mT\x1b[0m']
    with raises(SystemExit):
        assert check("WORD","WORD")


def test_get_n(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "5")
    assert get_n() == 5

    inputs = iter(["five", "16", "5"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert get_n() == 5

def test_get_guess(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "coded")
    assert get_guess(5) == "CODED"

    inputs = iter(["abcdefg", "abc", "icecream"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert get_guess(8) == "ICECREAM"
