import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)


class Pizza(Prototype):
    def __init__(self, size: int, ingredients: list[str], price: float) -> None:
        self.size = size
        self.ingridients = ingredients
        self.price = price

    def __str__(self) -> str:
        return f'Pizza{{size: {self.size} sm, ingridients: {self.ingridients}, price: {self.price}$}}'


if __name__ == '__main__':
    peperoni = Pizza(30, ['sausage', 'dough', 'mayonnaise'], 30)
    print(peperoni)

    clone_peperoni = peperoni.clone()
    clone_peperoni.ingridients.append('pepper')
    print(clone_peperoni)
