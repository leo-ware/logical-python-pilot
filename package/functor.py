from package.logical import Logical


class Functor(Logical):
    def __init__(self, name, *args):
        self.name = name
        self.args = list(args)

    def __repr__(self):
        return f"<Functor {self.name}({self.args})>"

    def unify_functor(self, thing):
        assert isinstance(thing, Functor)
        return all([
            self.name == thing.name,
            len(self.args) == len(thing.args),
            all([self.args[i] == thing.args[i] for i in range(len(self.args))])
        ])

    def __eq__(self, thing):
        if isinstance(thing, Functor):
            return self.unify_functor(thing)
        elif isinstance(thing, Variable) and not thing.bound:
            return thing == self
        elif isinstance(thing, Logical):
            return self == thing.value
        else:
            raise ValueError
