from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = Baratheon.__name__
        self.eyes = 'brown'
        self.hairs = 'dark'

    def die(self):
        """ """
        self.is_alive = False

    def __str__(self) -> str:
        return f'Vector: \
(\'{self.family_name}\', \'{self.eyes}\', \'{self.hairs}\')'

    def __repr__(self) -> str:
        return f'Vector: \
(\'{self.family_name}\', \'{self.eyes}\', \'{self.hairs}\')'


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = Lannister.__name__
        self.eyes = 'blue'
        self.hairs = 'light'

    @staticmethod
    def create_lannister(first_name, is_alive=True):
        return Lannister(first_name, is_alive)

    def die(self):
        self.is_alive = False

    def __str__(self) -> str:
        return f'Vector: \
(\'{self.family_name}\', \'{self.eyes}\', \'{self.hairs}\')'

    def __repr__(self) -> str:
        return f'Vector: \
(\'{self.family_name}\', \'{self.eyes}\', \'{self.hairs}\')'
