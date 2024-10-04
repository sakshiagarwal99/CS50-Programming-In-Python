from bank import value

def test_hello():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("Hello, World") == 0

def test_h():
    assert value("Howdy") == 20
    assert value("Hola") == 20

def test_without():
    assert value("Namaste") == 100
    assert value("Khama Ghani") == 100
