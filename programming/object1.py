from programming.object import add_posfix, mod_lista

if __name__ == '__main__':
    print(add_posfix(11))
    print(add_posfix("napis"))
    print(add_posfix([1, 2, 3]))
    print("###")
    lista = ["napis", ["jeden", "dwa"]]
    print(mod_lista(lista))