class MyIterator:
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._collection):
            value = self._collection[self._index]
            self._index += 1
            return value
        raise StopIteration

class MyCollection:
    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def __iter__(self):
        return MyIterator(self._items)

if __name__ == '__main__':
    collection = MyCollection()
    collection.add(1)
    collection.add(2)
    collection.add(3)
    collection.add(4)
    collection.add(5)

    for item in collection:
        print(f'{item}^2 = {item**2}')
