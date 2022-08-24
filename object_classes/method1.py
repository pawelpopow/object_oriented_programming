from object_classes.method import Write

if __name__ == '__main__':
    obj = Write("napis", 10)  # pomijamy argument self
    print(obj.write1)
    print(obj.number)
    print(obj.list)