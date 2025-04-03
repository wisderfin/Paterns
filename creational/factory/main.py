from abc import ABC, abstractmethod

class Food(ABC):
    @abstractmethod
    def get_recipe(self) -> str:
        pass

    @abstractmethod
    def get_energy_value(self, weigh: int = 100) -> dict:
        pass

class Pie(Food):
    def __init__(self):
        self.recipe = '''
            1. Смешайте муку, сахар и растопленное масло.
            2. Добавьте яйцо и перемешайте.
            3. Раскатайте тесто, положите начинку и сверните.
            4. Выпекайте при 180°C примерно 30-40 минут.
        '''
        self.protein = 3
        self.fat = 15
        self.carbohydrates = 45

    def get_recipe(self):
        return self.recipe

    def get_energy_value(self, weigh = 100):
        protein = self.protein / 100 * weigh
        fat = self.fat / 100 * weigh
        carbohydrates = self.carbohydrates / 100 * weigh

        return {
            'protein': protein,
            'fat': fat,
            'carbohydrates': carbohydrates
        }


class Pasta(Food):
    def __init__(self):
        self.recipe = '''
            1. Отварите 200 г пасты в подсоленной воде до состояния аль денте.
            2. На сковороде растопите 50 г сливочного масла, добавьте немного воды от варки пасты.
            3. Перемешайте пасту с маслом и посыпьте 50 г тёртого сыра (например, пармезана).
            4. Приправьте солью, перцем и подавайте.
        '''
        self.protein = 5
        self.fat = 1
        self.carbohydrates = 30

    def get_recipe(self):
        return self.recipe

    def get_energy_value(self, weigh = 100):
        protein = self.protein / 100 * weigh
        fat = self.fat / 100 * weigh
        carbohydrates = self.carbohydrates / 100 * weigh

        return {
            'protein': protein,
            'fat': fat,
            'carbohydrates': carbohydrates
        }

class Cooking:
    def render(self):
        food = self.create_food()
        print('Рецепт:')
        print(food.get_recipe())
        print("Энергетическая ценность на 100 г:")
        print(food.get_energy_value())

    @abstractmethod
    def create_food(self) -> Food:
        pass

class PieCooking(Cooking):
    def create_food(self):
        return Pie()

class PastaCooking(Cooking):
    def create_food(self):
        return Pasta()

if __name__ == '__main__':
    pie_cooking = PieCooking()
    pie_cooking.render()

    pasta_cooking = PastaCooking()
    pasta_cooking.render()
