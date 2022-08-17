class Write:
    def __init__(self, np1, value):
        self.write1 = np1
        self.number = value  # pomijamy sprawdzanie typów
        self.list = [1, 0, 2]


if __name__ == '__main__':
    obj = Write("napis", 10)  # pomijamy argument self
    print(obj.write1)
    print(obj.number)
    print(obj.list)
