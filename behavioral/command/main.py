from abc import ABC, abstractmethod

class Calculator:
    def __init__(self):
        self.history = [0]

    def new_result(self, new_result: float | int) -> None:
        self.history.append(new_result)

    def get_result(self) -> float | int:
        return self.history[-1]

    def undo(self) -> None:
        if len(self.history) < 2:
            raise Exception('The operation is not possible')
        self.history.pop()


class Operation(ABC):
    def __init__(self, x: float | int):
        self.x = x

    @abstractmethod
    def execute(self, calc: Calculator):
        pass

    def undo(self, calc: Calculator):
        calc.undo()


class AddOperation(Operation):
    def execute(self, calc: Calculator):
        calc.new_result(calc.get_result() + self.x)


class SubtractOperation(Operation):
    def execute(self, calc: Calculator):
        calc.new_result(calc.get_result() - self.x)


class MultiplyOperation(Operation):
    def execute(self, calc: Calculator):
        calc.new_result(calc.get_result() * self.x)


class DevideOperation(Operation):
    def execute(self, calc: Calculator):
        if self.x == 0:
            raise Exception('Zero division')
        calc.new_result(calc.get_result() / self.x)


class CalculatorControler:
    def __init__(self, calc: Calculator):
        self._undo: list[Operation] = []
        self._redo: list[Operation] = []
        self._calc: Calculator = calc

    def execute_operation(self, operation: Operation):
        operation.execute(self._calc)
        self._undo.append(operation)
        self._redo.clear()

    def undo(self):
        if self._undo:
            operation = self._undo.pop()
            operation.undo(self._calc)
            self._redo.append(operation)

    def redo(self):
        if self._redo:
            operation = self._redo.pop()
            operation.execute(self._calc)
            self._undo.append(operation)

    def result(self):
        return self._calc.get_result()

if __name__ == '__main__':
    calc = Calculator()
    controller = CalculatorControler(calc)

    print(controller.result())
    controller.execute_operation(AddOperation(15))
    print(controller.result())
    controller.execute_operation(DevideOperation(5))
    print(controller.result())
    controller.execute_operation(MultiplyOperation(5))
    print(controller.result())
    controller.execute_operation(SubtractOperation(3))
    controller.undo()
    print(controller.result())
    controller.redo()
    print(controller.result())
