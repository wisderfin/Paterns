from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def cooking(self) -> None:
        pass

class Drink(ABC):
    @abstractmethod
    def cooking(self) -> None:
        pass

class AmericanFood(Food):
    def cooking(self) -> None:
        print('BURGER')

class AmericanDrink(Drink):
    def cooking(self) -> None:
        print('COKE')

class ItalianFood(Food):
    def cooking(self) -> None:
        print('PIZZA')

class ItalianDrink(Drink):
    def cooking(self) -> None:
        print('WINE')

class Factory(ABC):
    @abstractmethod
    def create_food(self) -> Food:
        pass

    @abstractmethod
    def create_drink(self) -> Drink:
        pass

class AmericanFactory(Factory):
    def create_food(self) -> Food:
        return AmericanFood()

    def create_drink(self) -> Drink:
        return AmericanDrink()

class ItalianFactory(Factory):
    def create_food(self) -> Food:
        return ItalianFood()

    def create_drink(self) -> Drink:
        return ItalianDrink()

class Application:
    def __init__(self, factory: Factory) -> None:
        self.factory: Factory = factory
        self.food: Food = None
        self.drink: Drink = None

    def create(self) -> None:
        self.food = self.factory.create_food()
        self.drink = self.factory.create_drink()

    def cooking(self) -> None:
        self.food.cooking()
        self.drink.cooking()

class ApplicationConfigurator:
    def main(self) -> None:
        config = {'country': 'America'}

        if config['country'] == 'America':
            factory = AmericanFactory()
        elif config['country'] == 'Italy':
            factory = ItalianFactory()
        else:
            raise Exception('Unknown country')

        app = Application(factory)
        app.create()
        app.cooking()

if __name__ == '__main__':
    confugurator = ApplicationConfigurator()
    confugurator.main()
