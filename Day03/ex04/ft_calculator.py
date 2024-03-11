class calculator:
    """ """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        print('Dot product is:',
              sum([V1[i] * V2[i] for i in range(len(V1))]))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        print('Add Vector is :',
              [float(V1[i] + V2[i]) for i in range(len(V1))])

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        print('Sous Vector is:',
              [float(V1[i] - V2[i]) for i in range(len(V1))])
