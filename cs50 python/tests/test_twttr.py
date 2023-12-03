from twttr import short

def test_upper():
    assert short("TEST") == "TST"
    assert short("CAAAT") == "CT"

def test_lower():
    assert short("twitter") == "twttr"
    assert short("facebook") == "fcbk"

def test_num():
    assert short("53") == "53"

def test_empty():
    assert short("") == ""