from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass


class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str):
        self.number = card_number

    def pay(self, amount):
        print(f'Оплата картой {self.number} на {amount}$')


class CryptoPayment(PaymentStrategy):
    def __init__(self, wallet: str):
        self.wallet = wallet

    def pay(self, amount):
        print(f'Оплата криптовалютой({self.wallet}) на сумму {amount}$')


class SBPPayment(PaymentStrategy):
    def __init__(self, number: str):
        self.number = number

    def pay(self, amount):
        print(f'Оплата через СБП({self.number}) на сумму {amount}$')


class Order:
    def __init__(self, amount: float):
        self.amount = amount
        self.payment_strategy: PaymentStrategy = None

    def set_payment(self, strategy: PaymentStrategy) -> None:
        self.payment_strategy = strategy

    def pay(self):
        if not self.payment_strategy:
            raise Exception('Платежная система не установлена')
        self.payment_strategy.pay(self.amount)


if __name__ == '__main__':
    order_for_card = Order(10)
    order_for_card.set_payment(CreditCardPayment('5555-5555-5555-5555'))

    order_for_crypto = Order(145.9)
    order_for_crypto.set_payment(CryptoPayment('0xAAAAAAAAAAAAAAAAAAA'))

    order_for_spb = Order(12.04)
    order_for_spb.set_payment(SBPPayment('+79000000000'))

    order_for_card.pay()
    order_for_crypto.pay()
    order_for_spb.pay()
