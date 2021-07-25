
class Dungeon:

    def __init__(self):
        return


class Room(Dungeon):

    def __init__(self):
        super().__init__()
        self.__number = 0
        return

    def examplemethod(self):
        return self

    @classmethod
    def exampleclsmethod(cls):
        return cls()

    @staticmethod
    def examplestaticmethod():
        print("This doesn't do anything to the class")
        return True

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, val):
        self.__number = val
