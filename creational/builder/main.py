from abc import ABC, abstractmethod

class User:
    def __init__(self):
        self.name = None
        self.email = None
        self.language = None

    def __str__(self):
        return f'User[name:{self.name}, email:{self.email}, language:{self.language}]'

class Builder(ABC):
    @abstractmethod
    def new(self) -> None:
        pass

    @abstractmethod
    def set_name(self, name: str) -> None:
        pass

    @abstractmethod
    def set_email(self, email: str) -> None:
        pass

    @abstractmethod
    def set_language(self, language: str) -> None:
        pass

    def get(self) -> User:
        pass

class UserBuilder(Builder):
    def __init__(self) -> None:
        self.new()

    def new(self):
        self.user = User()

    def set_name(self, name):
        self.user.name = name

    def set_email(self, email):
        self.user.email = email

    def set_language(self, language):
        self.user.language = language

    def get(self) -> User:
        return self.user

class Director:
    def create_russian_user(self, builder: Builder) -> None:
        builder.new()
        builder.set_name('Ivan')
        builder.set_email('ivan@example.com')
        builder.set_language('Russian')

    def create_english_user(self, builder: Builder) -> None:
        builder.new()
        builder.set_name('John')
        builder.set_email('john@example.com')
        builder.set_language('English')

if __name__ == '__main__':
    builder = UserBuilder()
    director = Director()

    director.create_russian_user(builder)
    ru_user = builder.get()
    print(ru_user)

    director.create_english_user(builder)
    en_user = builder.get()
    print(en_user)
