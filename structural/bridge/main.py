from abc import ABC, abstractmethod


class CalculatorImpl(ABC):
    @abstractmethod
    def addition(self, x: str, y: str) -> str:
        pass

    @abstractmethod
    def subtraction(self, x: str, y: str) -> str:
        pass

    @abstractmethod
    def multiplication(self, x: str, y: str) -> str:
        pass


class BINCalculatorImpl(CalculatorImpl):
    def addition(self, x: str, y: str) -> str:
        return bin(int(x, 2) + int(y, 2))

    def subtraction(self, x: str, y: str) -> str:
        return bin(int(x, 2) - int(y, 2))

    def multiplication(self, x: str, y: str) -> str:
        return bin(int(x, 2) * int(y, 2))


class DECCalculatorImpl(CalculatorImpl):
    def addition(self, x: str, y: str) -> str:
        return str(int(x) + int(y))

    def subtraction(self, x: str, y: str) -> str:
        return str(int(x) - int(y))

    def multiplication(self, x: str, y: str):
        return str(int(x) * int(y))


class HEXCalculatorImpl(CalculatorImpl):
    def addition(self, x: str, y: str) -> str:
        return hex(int(x, 16) + int(y, 16))[2:].upper()

    def subtraction(self, x: str, y: str) -> str:
        return hex(int(x, 16) - int(y, 16))[2:].upper()

    def multiplication(self, x: str, y: str) -> str:
        return hex(int(x, 16) * int(y, 16))[2:].upper()


class Calculator:
    def __init__(self, impl: CalculatorImpl):
        self.impl = impl

    def addition(self, x: str, y: str) -> str:
        return self.impl.addition(x, y)

    def subtraction(self, x: str, y: str) -> str:
        return self.impl.subtraction(x, y)

    def multiplication(self, x: str, y: str) -> str:
        return self.impl.multiplication(x, y)


if __name__ == '__main__':
    bin_x = '1100'
    bin_y = '101'
    dec_x = '10'
    dec_y = '2'
    hex_x = 'B2C'
    hex_y = 'AB3'

    bin_calc = Calculator(BINCalculatorImpl())
    dec_calc = Calculator(DECCalculatorImpl())
    hex_calc = Calculator(HEXCalculatorImpl())

    print(f'{bin_x} + {bin_y} = {bin_calc.addition(bin_x, bin_y)}')
    print(f'{bin_x} - {bin_y} = {bin_calc.subtraction(bin_x, bin_y)}')
    print(f'{bin_x} * {bin_y} = {bin_calc.multiplication(bin_x, bin_y)}')

    print(f'{dec_x} + {dec_y} = {dec_calc.addition(dec_x, dec_y)}')
    print(f'{dec_x} - {dec_y} = {dec_calc.subtraction(dec_x, dec_y)}')
    print(f'{dec_x} * {dec_y} = {dec_calc.multiplication(dec_x, dec_y)}')

    print(f'{hex_x} + {hex_y} = {hex_calc.addition(hex_x, hex_y)}')
    print(f'{hex_x} - {hex_y} = {hex_calc.subtraction(hex_x, hex_y)}')
    print(f'{hex_x} * {hex_y} = {hex_calc.multiplication(hex_x, hex_y)}')
