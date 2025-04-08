import math
from abc import ABC, abstractmethod


class Expression(ABC):
    @abstractmethod
    def evaluate(self) -> float:
        pass


class Number(Expression):
    def __init__(self, value: float):
        self.value = value

    def evaluate(self) -> float:
        return self.value


class ExpressionDecorator(Expression):
    def __init__(self, expr: Expression):
        self.expr = expr


class Abs(ExpressionDecorator):
    def evaluate(self) -> float:
        return abs(self.expr.evaluate())


class Square(ExpressionDecorator):
    def evaluate(self) -> float:
        return self.expr.evaluate()**2


class SquareRoot(ExpressionDecorator):
    def evaluate(self) -> float:
        if self.expr.evaluate() < 0:
            raise Exception('Number is too low')
        return self.expr.evaluate()**0.5


class BinaryLog(ExpressionDecorator):
    def evaluate(self) -> float:
        if self.expr.evaluate() <= 0:
            raise Exception('Number is too low')
        return math.log(self.expr.evaluate(), 2)


class Inc(ExpressionDecorator):
    def evaluate(self) -> float:
        return self.expr.evaluate() + 1

class Halve(ExpressionDecorator):
    def evaluate(self) -> float:
        return self.expr.evaluate() / 2

if __name__ == '__main__':
    expr = Number(-20)
    print(f'number: {expr.evaluate()}')

    expr = Abs(expr)
    print(f'abs: {expr.evaluate()}')

    expr = Square(expr)
    print(f'square: {expr.evaluate()}')

    expr = SquareRoot(expr)
    print(f'square root: {expr.evaluate()}')

    expr = BinaryLog(expr)
    print(f'binary log: {expr.evaluate()}')

    expr = Inc(expr)
    print(f'inc: {expr.evaluate()}')

    expr = Halve(expr)
    print(f'halve: {expr.evaluate()}')
