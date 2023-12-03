from numb3rs import validate

def test_true():
    assert validate("1.2.3.4") == "True"
    assert validate("127.0.0.1") == "True"

def test_false():
    assert validate("275.255.255.0") == "False"
    assert validate("0.0.0.999") == "False"