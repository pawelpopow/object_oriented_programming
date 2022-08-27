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

    def _name(self):
        '''metoda z założenia chroniona jedynie do wykorzystania w klasach potomnych'''
        return self.__name

    def _county(self):
        '''metoda z założenia chroniona jedynie do wykorzystania w klasach potomnych'''
        return self.__county

    def _firstname(self):
        '''metoda z założenia chroniona jedynie do wykorzystania w klasach potomnych'''
        return self.firstname

    def _phone(self):
        '''metoda z założenia chroniona jedynie do wykorzystania w klasach potomnych'''
        return self._phone


class City(Town):
    def __init__(self, name, county, firstname, phone):
        super().__init__(name, county, firstname, phone)

    def location(self):
        print('Miasto i gmina {0:%>s}, powiat {1:%>s}'.format(self._name(), self._county()))
