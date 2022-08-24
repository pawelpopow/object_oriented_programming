from class_decorators.property import Variable

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