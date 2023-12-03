from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_str():
    jar = Jar()
    jar.deposit(4)
    assert str(jar) == "🍪🍪🍪🍪"
    jar.withdraw(2)
    assert str(jar) == "🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(4)
    assert jar.size == 4

def test_withdraw():
    jar = Jar()
    jar.deposit(4)
    jar.withdraw(2)
    assert jar.size == 2