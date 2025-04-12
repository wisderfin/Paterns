from abc import ABC, abstractmethod

class ATMState(ABC):
    def __init__(self, atm: 'ATM') -> None:
        self.atm = atm

    @abstractmethod
    def insert_card(self) -> None:
        pass

    @abstractmethod
    def enject_card(self) -> None:
        pass

    @abstractmethod
    def enter_pin(self, pin: str) -> None:
        pass

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass


class NoCardState(ATMState):
    def insert_card(self):
        print('Карта вставлена')
        self.atm.set_state(self.atm.has_card_state)

    def enject_card(self):
        print('Нет карты для извлечения')

    def enter_pin(self, pin):
        print('Сначала вставьте крату')

    def withdraw(self, amount):
        print('Сначала вставьте карту')

class HasCardState(ATMState):
    def insert_card(self):
        print('Карта уже вставлена')

    def enject_card(self):
        print('Карта извлечена')
        self.atm.set_state(self.atm.no_card_state)

    def enter_pin(self, pin):
        if pin == '1234':
            self.atm.set_state(self.atm.authorizated_state)
            print('PIN верный')
        else:
            print('PIN неверный')

    def withdraw(self, amount):
        print('Сначала введите PIN')

class AuthorizatedState(ATMState):
    def insert_card(self):
        print('Карта уже вставлена')

    def enject_card(self):
        print('Карта извлечена')
        self.atm.set_state(self.atm.no_card_state)

    def enter_pin(self, pin):
        print('Вы уже авторизованы')

    def withdraw(self, amount):
        print (f'Выведено {amount}$')

class ATM:
    def __init__(self) -> None:
        self.no_card_state = NoCardState(self)
        self.has_card_state = HasCardState(self)
        self.authorizated_state = AuthorizatedState(self)

        self.current_state = self.no_card_state

    def set_state(self, state: ATMState) -> None:
        self.current_state = state

    def insert_card(self) -> None:
        self.current_state.insert_card()

    def eject_card(self) -> None:
        self.current_state.enject_card()

    def enter_pin(self, pin: str) -> None:
        self.current_state.enter_pin(pin)

    def withdraw(self, amount: float) -> None:
        self.current_state.withdraw(amount)

if __name__ == '__main__':
    atm = ATM()

    atm.insert_card()
    atm.withdraw(1000)
    atm.enter_pin('1234')
    atm.withdraw(1500)
    atm.eject_card()
    atm.enter_pin('1234')

