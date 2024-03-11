class calculator:
    """ """

    def __init__(self, vector) -> None:
        self.vector = vector

    def __add__(self, val) -> None:
        self.vector = [i + val for i in self.vector]
        print(self.vector)

    def __mul__(self, val) -> None:
        self.vector = [i * val for i in self.vector]
        print(self.vector)

    def __sub__(self, val) -> None:
        self.vector = [i - val for i in self.vector]
        print(self.vector)

    def __truediv__(self, val) -> None:
        if val == 0:
            print('Error: Division by 0')
        else:
            self.vector = [i / val for i in self.vector]
            print(self.vector)
