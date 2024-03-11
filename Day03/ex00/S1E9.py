from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class Character"""

    @abstractmethod
    def __init__(self):  # , first_name, is_alive=True):
        """Your docstring for Constructor Character"""
        pass

    @abstractmethod
    def die(self):
        """Your docstring for Method die Character"""
        pass


class Stark(Character):
    """Your docstring for Class Stark"""

    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Your docstring for Method die"""
        self.is_alive = False
