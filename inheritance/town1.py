from inheritance.town import Town

if __name__ == '__main__':
    town1 = Town("Luboń", "Poznański", "Jacek", "632323437")
    # town2 = Town("Pomorskie", "Gdansk", "Bartek", "5234432532")
    # town3 = Town("Slaskie", "Wrocław", "Ala", "645323523")
    town1.location()
    # town2.location()
    # town3.location()
    print(type(town1))
    # print(type(town2))
    # print(type(town3))

    # Luboń, county poznański
    # Pomorskie, county Gdansk
    # Slaskie, county Wrocław
