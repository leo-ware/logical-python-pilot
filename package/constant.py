from package.logical import Logical


class Constant(Logical):
    """Python class representing a package constant

    Args:
        value (any, optional): value of the constant, defaults to a randomly generated string

    Examples:
        >>> leo = Constant("Leo")
        >>> leo == leo
        True
        >>> leo == "Leo"  # because we specified "Leo" as the value
        True
        >>> "leo" == leo
        True
        >>> leo == "andre"
        False

        >>> andre = Constant()
        >>> andre == leo
        False
        >>> andre == "Andre"  # we didn't specify a value
        False

        # constants can hold arbitrary datatypes
        >>> pi = Constant(3.14159)
        >>> pi == 3.14159
        True
    """

    def __init__(self, value=None):
        self._value = value if value else self.placeholder_name("constant")

    def __repr__(self):
        return f'<Constant value="{self.value}">'

    @property
    def value(self):
        return self._value

    def __eq__(self, thing):
        """unification operator for package Constants
        Note:
            This is the unification operator, not an equality check. It can sometimes cause state
            changes when applied to a Variable. See the docstring for ```Variable.__eq__``` for
            more.
        """
        if isinstance(thing, self.__class__):
            return self.value == thing.value
        elif isinstance(thing, Logical):
            return thing == self
        else:
            return self.value == thing
