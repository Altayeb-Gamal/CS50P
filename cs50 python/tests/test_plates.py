from plates import is_valid


def test_len():
    assert is_valid("A") == False
    assert is_valid("AAaaaaa") == False

def test_isfirst_0():
    assert is_valid("Cs50") == True
    assert is_valid("0CS") == False

def test_punct():
    assert is_valid("AAa,a") == False
    assert is_valid("AAa,.") == False

def test_first2lett():
    assert is_valid("3A") == False
    assert is_valid("A3") == False

def test_scndhf_isnum():
    assert is_valid("Abc3d") == False
    assert is_valid("Ab55c") == False

