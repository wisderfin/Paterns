from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def render(self, indent: int = 0) -> None:
        pass


class File(Item):
    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url

    def render(self, indent: int = 0) -> None:
        print(f'{" " * indent}- {self.url}/{self.name}')


class Directory(Item):
    def __init__(self, name: str):
        self.name = name
        self.children: list[Item] = []

    def add(self, item: Item) -> None:
        self.children.append(item)

    def remove(self, item: Item) -> None:
        self.children.remove(item)

    def render(self, indent: int = 0) -> None:
        print(f'{" " * indent}- [{self.name}]')
        for child in self.children:
            child.render(indent + 2)

if __name__ == '__main__':
    javascript = File('script.js', '/javascript')
    python = File('main.py', '/python')
    c = File('main.c', '/c')
    h = File('main.h', '/c')
    cs = File('main.cs', '/c#')

    main_menu = Directory("Projects")
    main_menu.add(python)
    main_menu.add(javascript)
    main_menu.add(c)
    main_menu.add(h)
    main_menu.add(cs)

    main_menu.render()
