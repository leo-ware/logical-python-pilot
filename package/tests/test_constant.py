from package import Constant


def test_equality():
    a = Constant()
    b = Constant()
    assert a == a
    assert not b == a  # will fail on hash collision


def test_value_assignment():
    a = Constant("A")
    assert a == "A"
    assert a.value == "A"
    assert a.__repr__() == '<Constant value="A">'
