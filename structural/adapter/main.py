import math

class CartesianPoint:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance(self) -> float:
        return (self.x**2 + self.y**2)**0.5

    def __str__(self):
        return f'CartesianPoint{{x: {self.x}, y: {self.y}}}'


class PolarPoint:
    def __init__(self, radius: float, degree: float):
        self.radius = radius
        self.degree = degree

class PolarToCartesianAdapter:
    def __init__(self, polar: PolarPoint):
        self.polar = polar

    def get_carties(self) -> CartesianPoint:
        radians = math.radians(self.polar.degree)
        x = self.polar.radius * math.cos(radians)
        y = self.polar.radius * math.sin(radians)
        return CartesianPoint(x, y)

if __name__ == '__main__':
    cartesian = CartesianPoint(3, 4)
    polar = PolarPoint(1, 1)

    polar_to_cartesian = PolarToCartesianAdapter(polar).get_carties()

    print(f'cartesian: {cartesian.distance()}')
    print(f'polar_to_cartesian: {polar_to_cartesian.distance()}')
