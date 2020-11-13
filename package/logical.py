import random


class Logical:
    """Static parent class for classes in the module
    """
    @staticmethod
    def placeholder_name(base="item"):
        """ Generates (probably) unique filler value
        Args:
            base (str): string to put at the front so humans can identify
        """
        return f"{base}-{hash(random.random())}"
