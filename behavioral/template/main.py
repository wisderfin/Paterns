from abc import ABC, abstractmethod

class Beverage(ABC):
    def prepare(self):
        self.boil_water()
        self.pour_in_cup()
        self.brew()
        self.add_ingredients()

    def boil_water(self) -> None:
        print('Кипятим воду')

    def pour_in_cup(self) -> None:
        print('Наливаем воду в чашку')

    @abstractmethod
    def brew(self) -> None:
        pass

    @abstractmethod
    def add_ingredients(self) -> None:
        pass

class Tea(Beverage):
    def brew(self):
        print('Завариваем чай')

    def add_ingredients(self):
        print('Добавляем лимон')

class Coffee(Beverage):
    def brew(self):
        print('Завариваем кофе')

    def add_ingredients(self):
        print('Добавляем молоко')


if __name__ == '__main__':
    tea = Tea()
    tea.prepare()

    coffee = Coffee()
    coffee.prepare()
