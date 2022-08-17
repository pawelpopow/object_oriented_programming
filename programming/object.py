def add_posfix(strg):
    # return str(strg) + '_postfix'
    # return str(strg) + '_next'
    return str(strg) + '_programming'


def mod_lista(lista):
    # return str(lista[0]) + "_" + str(lista[1][1])
    # return str(lista[0]) + "  " + str(lista[1][1])
    return str(lista[0]) + "," + str(lista[1][1])


if __name__ == '__main__':
    print(add_posfix(11))
    print(add_posfix("napis"))
    print(add_posfix([1, 2, 3]))
    print("###")
    lista = ["napis", ["jeden", "dwa"]]
    print(mod_lista(lista))
