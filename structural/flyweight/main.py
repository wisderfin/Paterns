class CarType:
    def __init__(self, brand: str, model: str, color: str):
        self.brand = brand
        self.model = model
        self.color = color

    def render(self, x, y) -> None:
        print(f'Car{{brand: {self.brand}, model: {self.model}, color: {self.color}, x: {x}, y: {y}}}')


class CarFactory:
    _car_types = {}

    @classmethod
    def get_car_type(cls, brand: str, model: str, color: str) -> CarType:
        key = (brand, model, color)
        if key not in cls._car_types:
            cls._car_types[key] = CarType(brand, model, color)
        return cls._car_types[key]


class Car:
    def __init__(self, x: int, y: int, car_type: CarType):
        self.x = x
        self.y = y
        self.car_type = car_type

    def render(self) -> None:
        self.car_type.render(self.x, self.y)

class Parking:
    def __init__(self):
        self.cars: list[Car] = []

    def assemble_car(self, x: int, y: int, brand: str, model: str, color: str) -> None:
        car_type = CarFactory.get_car_type(brand, model, color)
        car = Car(x, y, car_type)
        self.cars.append(car)

    def render_parking(self):
        for car in self.cars:
            car.render()

if __name__ == '__main__':
    parking = Parking()
    parking.assemble_car(1, 1, 'toyota', 'carola', 'silver')
    parking.assemble_car(3, 5, 'mercedes', 'benz', 'black')
    parking.assemble_car(4, 6, 'lamborghini', 'urus', 'gold')

    parking.render_parking()
