class MyDict:
    keys = None
    values = None
    length = None
    dict = dict()

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def get_item(self):
        dict[self.key] = self.value


p1 = MyDict("apple", 15)
print(p1.__dict__)
