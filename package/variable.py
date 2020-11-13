from package import Logical


class Variable(Logical):
    """Class for representing package variables
    Args:
        value (any, optional): initializes the variable with this value --- not recommended, you
        should probably use Constant for this

    Attributes:
        bound (bool): whether the variable is bound
        references (List[Variable]): list of variables that must be notified on binding

    Note:
        Variables cannot initialize with a binding to None. I.e., '''Variable(None)''' will
        return an unbound variable. If you need to bind a variable to '''None''', first initialize
        the variable and then set it to '''None'''.

    Examples:
        >>> x = Variable("foo")
        >>> x == "foo"
        True
        >>> x == x
        True

        >>> y = Variable()
        >>> y == "foo" # y binds to "foo"
        True
        >>> y == "bar"
        False
        >>> y.value
        "foo"
    """

    def __init__(self, value=None):
        self._value = Variable.Pointer(value)
        self.bound = value is not None
        self.references = []

    def __repr__(self):
        return f"<Variable {'' if self.bound else 'un'}bound value={self._value.get_value()}>"

    class Pointer:
        """Class for keeping track of variable pointers
        It might seem like we should just use a raw value here, but using a Pointer means we
        can support circular assignment, and variables lazy loading values (staying updated)
        """

        def __init__(self, to):
            self.to = to

        def __repr__(self):
            return f"<Pointer to={self.get_value()}>"

        def get_value(self, _traversed=None):
            """Tries to figure out what the actual value is here
            Too complicated, there are probably bugs.
            """

            _traversed = _traversed if (_traversed is not None) else set()
            if self in _traversed:
                return "**circular definition**"
            _traversed.add(self)

            # if we point to a pointer, recursive call
            if isinstance(self.to, Variable.Pointer):
                return self.to.get_value(_traversed=_traversed)

            # if we point to a variable, recursive call to its pointer
            elif isinstance(self.to, Variable):
                return self.to._value.get_value(_traversed=_traversed)

            # else just return pointer value
            else:
                return self.to

    @property
    def value(self):
        """value of the variable (returns **circular definition** when defined in terms of unbound variables)
        """
        return self._value.get_value()

    def bind(self):
        """Binds variables and recursively binds references
        """
        print(f"Binding {self}")  # debug
        self.bound = True
        for ref in self.references:
            print(f"Removing reference from {ref}")
            ref.references.remove(self)
            ref.bind()

    def __eq__(self, thing):
        """Unification operator for variables
        Attempts to unify the variable with another object. If the variable is bound, and the other
        value is not an unbound variable, it will attempt to compare equality. If either value
        in a unification is an unbound variable, the unbound variable's value will become a pointer
        to the other value. And, unless the other value is also an unbound variable, it will become
        bound.

        If both parameters to unification are unbound variables, each receives a pointer to other,
        but they remain unbound. If one of them is a assigned a value later, they both become bound.

        Note:
            This is the unification operator, *not* an equality check. Variable state may change
            when you call this function. You have been warned.
        """
        if self.bound:
            # this kind of seems like a lot of if statements, maybe I should simplify somehow
            try:
                thing_class_name = thing.__class__.__name__
            except AttributeError:
                thing_class_name = "huh, that's weird"

            # it's a variable
            if thing_class_name == "Variable":
                if not thing.bound:
                    return thing == self
                else:
                    return self.value == thing.value

            # it's a constant
            elif thing_class_name == "Constant":
                return self.value == thing.value

            # it's a functor
            elif thing_class_name == "Functor":
                return thing == self.value

            # it's not a logical datatype
            else:
                return thing == self.value

        # It's not bound. So, we bind and return True.
        self._value = Variable.Pointer(thing)

        # Complicated things to do it's also an unbound variable.
        if isinstance(thing, Variable) and not thing.bound:
            thing._value = Variable.Pointer(self)
            thing.references.append(self)
            self.references.append(thing)
        else:
            self.bind()

        return True
