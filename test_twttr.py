from twttr import shorten

def test_withvowels():
    assert shorten("Wonderful") == "Wndrfl"
    assert shorten("COMPUTER") == "CMPTR"
    assert shorten("Hello, World") == "Hll, Wrld"
def test_withoutvowels():
    assert shorten("Cry") == "Cry"
    assert shorten("Hym") == "Hym"
def test_numbers():
    assert shorten("1") == "1"
    assert shorten("1000") == "1000"
