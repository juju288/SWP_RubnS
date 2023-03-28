import random

class arraylist:
    def __init__(self):
        self.list = []

    def append(self, data):
        self.list.append(data)

    def appendMultiple(self, *data):
        for d in data:
            self.append(d)

    def appendRandoms(self, anz, limit):
        for i in range(anz):
            self.append(int(random.random() * limit))

    def insert(self, pos, data):
        self.list.insert(pos, data)

    def insertMultiple(self, pos, data):
        i = pos
        for d in data:
            self.list.insert(i, data)
            i = i + 1

    def length(self):
        return self.list.count()

    def showData(self):
        return self.list.__str__()

    def delete(self, pos):
        self.list.pop(pos)

    def pop(self):
        self.list.pop()

    def reverse(self):
        self.list.reverse()

    def clear(self):
        self.list = []

    def search(self, id):
        self.list.index(id)

    def sort(self):
        self.list.sort()


def main():
    lst = arraylist()

    lst.appendRandoms(16, 10)
    print(lst.showData())

    lst.sort()
    print(lst.showData())


if __name__ == "__main__":
    main()