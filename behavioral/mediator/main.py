from abc import ABC, abstractmethod


class ChatMediator(ABC):
    @abstractmethod
    def send_message(self, message: str, user: "User") -> None:
        pass


class ChatRoom(ChatMediator):
    def __init__(self):
        self.users = []

    def register(self, user: "User"):
        self.users.append(user)

    def send_message(self, message: str, sender: "User") -> None:
        for user in self.users:
            if user != sender:
                user.receive(message, sender.name)


class User:
    def __init__(self, name: str, mediator: ChatMediator):
        self.name = name
        self.mediator = mediator
        mediator.register(self)

    def send(self, message: str):
        print(f"{self.name} отправляет сообщение: {message}")
        self.mediator.send_message(message, self)

    def receive(self, message: str, sender_name: str):
        print(f"{self.name} получил сообщение от {sender_name}: {message}")


if __name__ == "__main__":
    chat = ChatRoom()

    user1 = User("Алиса", chat)
    user2 = User("Боб", chat)
    user3 = User("Чарли", chat)

    user1.send("Привет, ребята!")
    user2.send("Привет, Алиса!")
