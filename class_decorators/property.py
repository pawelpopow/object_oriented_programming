class Variable:
    def __init__(self):
        self.public = 10
        self._protected = 20
        self.__private1 = 30
        self.__privacy_double = self.__private1 * 2  # jest zależność między zmiennymi

    def privat_fetch2(self):
        return self.__privacy_double

    @property
    def private_variable(self):
        return self.__private1

    @private_variable.setter
    def private_variable(self, new_value):  # zmieniamy dwie waratości
        self.__private1 = new_value
        self.__privacy_double = self.__private1 * 2


if __name__ == '__main__':
    zm = Variable()
    print(zm)
    print(zm.private_variable)
    print(zm.public)
    print(zm.privat_fetch2)
    print(zm.__init__)
    print(zm._protected)
    print(zm.public*2)
    print(type(zm))
    print(type(zm.public))