from bank import greet

def test_hi():
    assert greet("Hi") == "$20"
    assert greet("hi") == "$20"

def test_hello():
    assert greet("Hello") == "$0"
    assert greet("hello") == "$0"

def test_yo():
    assert greet("Yo") == "$100"
    assert greet("yo") == "$100"