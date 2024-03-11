from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """ """
    def set_eyes(self, eye):
        self.eyes = eye

    def set_hairs(self, hair):
        self.hairs = hair

    def get_eyes(self):
        return self.eyes

    def get_hairs(self):
        return self.hairs
