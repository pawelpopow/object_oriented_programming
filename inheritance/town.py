# nie zakładamy sprawdzania zgodności typów
class Town:
    def __init__(self, name, county):
        self.__name = name  # zmienne prywatne, niedostępne do modyfikacji po zainicjowaniu
        self.__county = county

    def location(self):
        print(self.__name + ", powiat " + self.__county)
        print('To jest powiat: ' + self.__county)
        print('To województwo: ' + self.__name)

    def _county(self):
        '''metoda z założenia chroniona jedynie do wykorzystania w klasach potomnych'''
        return self.__county

    def _name(self):
        '''metoda z założenia chroniona jedynie do wykorzystania w klasach potomnych'''
        return self.__name


if __name__ == '__main__':
    town1 = Town("Luboń", "Poznański")
    town2 = Town("Pomorskie", "Gdansk")
    town3 = Town("Slaskie", "Wrocław")
    town1.location()
    town2.location()
    town3.location()

    # Luboń, county poznański
    # Pomorskie, county Gdansk
    # Slaskie, county Wrocław
