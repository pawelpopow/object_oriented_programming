# nie zakładamy sprawdzania zgodności typów
class Town:
    def __init__(self, name, county, firstname, phone):
        self.__name = name  # zmienne prywatne, niedostępne do modyfikacji po zainicjowaniu
        self.__county = county
        self.firstname = firstname
        self.phone = phone

    def location(self):
        print(self.__name + ", powiat " + self.__county)
        print('-------------------------------------------------------------------------------')
        print('To jest powiat: ' + self.__county)
        print('-------------------------------------------------------------------------------')
        print('To województwo: ' + self.__name)
        print('-------------------------------------------------------------------------------')
        print(
            'Mam na  imie: ' + self.firstname + ', mój powiat to: ' + self.__county + ', województwo: ' + self.__name +
            ', numerze: ' + self.phone)
        print('-------------------------------------------------------------------------------')

    def _county(self):
        '''metoda z założenia chroniona jedynie do wykorzystania w klasach potomnych'''
        return self.__county

    def _name(self):
        '''metoda z założenia chroniona jedynie do wykorzystania w klasach potomnych'''
        return self.__name


class City(Town):
    def __init__(self, name, county, firstname, phone):
        super().__init__(name, county, firstname, phone)

    def location(self):
        print('Miasto i gmina {0:%>s}, powiat {1:%>s}'.format(self._name(), self._county()))
        print('-------------------------------------------------------------------------------')


class Village(Town):
    def __init__(self, name, community, county, firstname, phone):
        super().__init__(name, county, firstname, phone)
        self.__community = community

    def location(self):
        print('{0:%>s}, gmina {1:%>s}, powiat {2:%>s}'.format(self._name(), self.__community, self._county()))
        print('-------------------------------------------------------------------------------')
