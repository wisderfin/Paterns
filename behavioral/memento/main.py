class ProfileMemento:
    def __init__(self, state: 'UserProfile') -> None:
        self.name = state.name
        self.email = state.email
        self.age = state.age


class ProfileHistory:
    def __init__(self):
        self._states: list[ProfileMemento] = []

    def backup(self, memento: ProfileMemento) -> None:
        self._states.append(memento)

    def undo(self) -> ProfileMemento:
        if len(self._states) < 2:
            raise IndexError('No states to restore.')
        self._states.pop()
        return self._states[-1]



class UserProfile:
    def __init__(self, name: str, email: str, age: int) -> None:
        self.name = name
        self.email = email
        self.age = age

    def edit_name(self, new_name: str) -> None:
        self.name = new_name

    def edit_email(self, new_email: str) -> None:
        self.email = new_email

    def edit_age(self, new_age: int) -> None:
        self.age = new_age

    def get_profile(self) -> dict:
        return {
            'name': self.name,
            'email': self.email,
            'age': self.age
        }

    def save(self) -> ProfileMemento:
        return ProfileMemento(self)

    def restore(self, memento: ProfileMemento):
        self.name = memento.name
        self.email = memento.email
        self.age = memento.age

if __name__ == '__main__':
    history = ProfileHistory()
    profile = UserProfile('wisderfin', 'wisderfin@yandex.ru', 20)

    history.backup(profile.save())
    print(profile.get_profile())

    profile.edit_name('wsdrfn')
    history.backup(profile.save())
    print(profile.get_profile())

    profile.restore(history.undo())
    print(profile.get_profile())
