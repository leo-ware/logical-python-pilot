from package import Functor


def test_instantiate():
    a = Functor("Mom", "Jane", "Henry")
    assert a == a
    assert a == Functor("Mom", "Jane", "Henry")
    assert a.name == "Mom"
    assert a.args == ["Jane", "Henry"]


def test_not_equal():
    a = Functor("Angry", "Joe")
    b = Functor("Angry", "Joe", "Kathleen")
    c = Functor("Sad", "Joe")
    assert a.name == b.name
    assert not a == b
    assert not a == c
