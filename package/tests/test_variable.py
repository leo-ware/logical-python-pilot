from package import Variable


def test_identity():
    x = Variable()
    assert not x.bound
    assert x == x


def test_init_with_value():
    x = Variable("foo")
    assert x.bound
    assert x == x
    assert x == 'foo'
    assert 'foo' == x
    assert x != 'bar'
    assert x.value == 'foo'


def test_circular_assignments():
    x = Variable()
    y = Variable()
    assert x == y
    assert not x.bound


def test_circular_bindings():
    x = Variable()
    y = Variable()
    z = Variable()

    assert x == y
    assert x == 'foo'
    assert y != 'bar'
    assert y.bound


def test_assignment_transitivity():
    x = Variable('foo')
    y = Variable()
    z = Variable()

    assert x == y
    assert y == z
    assert z.value == 'foo'


def test_assignment_transitivity_value_update():
    x = Variable()
    y = Variable()
    z = Variable()

    assert x == y
    assert y == z
    assert x == "foo"
    assert z == "foo"
