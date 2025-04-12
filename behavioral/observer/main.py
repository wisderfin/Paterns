class Follower:
    def __init__(self, name) -> None:
        self.name = name

    def update(self, message) -> None:
        print(f'{self.name} получил сообщение: "{message}"')

class Subject:
    def __init__(self) -> None:
        self._followers = []

    def follow(self, follower: Follower) -> None:
        self._followers.append(follower)

    def unfollow(self, follower: Follower) -> None:
        self._followers.remove(follower)

    def notify(self, message) -> None:
        for follower in self._followers:
            follower.update(message)

if __name__ == '__main__':
    subject = Subject()

    follower_1 = Follower('wsdrfn')
    follower_2 = Follower('wisderfin')

    subject.follow(follower_1)
    subject.follow(follower_2)

    subject.notify('Что-то важное')

    subject.unfollow(follower_1)

    subject.notify('Что-то не важное')
