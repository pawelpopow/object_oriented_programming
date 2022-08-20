# nie zakładamy sprawdzania zgodności typów
class Town:
    def __init__(self, name, county):
        self.__name = name  # zmienne prywatne, niedostępne do modyfikacji po zainicjowaniu
        self.__county = county

    def location(self):
        print(self.__name + ", county " + self.__county)

    def _county(self):
        '''metoda z założenia chroniona jedynie do wykorzystania w klasach potomnych'''
        return self.__county

    def _name(self):
        '''metoda z założenia chroniona jedynie do wykorzystania w klasach potomnych'''
        return self.__name


if __name__ == '__main__':
    town1 = Town("Luboń", "poznański")
    town1.location()
