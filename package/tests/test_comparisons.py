from package import Constant, Variable, Functor


def test_constant_variable():
    foo = Constant('foo')
    x = Variable()
    assert foo == x
    assert x == 'foo'


def test_functor_variable():
    x = Variable()
    assert Functor("Angry", x) == Functor("Angry", "Joe")
    assert x == "Joe"
