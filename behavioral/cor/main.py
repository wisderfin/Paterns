class Handler:
    def __init__(self):
        self.next = None

    def set_next(self, handler: 'Handler') -> 'Handler':
        self.next = handler
        return handler

    def handle(self, data: dict) -> 'Handler':
        if self.next:
            return self.next.handle(data)


class NameHandler(Handler):
    def handle(self, data: dict):
        name = data.get('name')
        if not name:
            raise Exception('ERROR: name is empty')
        return super().handle(data)


class EmailHandler(Handler):
    def handle(self, data: dict):
        email = data.get('email')
        if not email or '@' not in email:
            raise Exception('ERROR: email is invalid')
        return super().handle(data)


class PasswordHandler(Handler):
    def handle(self, data: dict):
        password = data.get('password')
        if not password or len(password) < 8:
            raise Exception('ERROR: password is too short')
        return super().handle(data)


if __name__ == '__main__':
    data = {
        'name': 'wisderfin',
        'email': 'wisderfin@yandex.ru',
        'password': 'SupperPupperPassword'
    }

    chain = NameHandler()
    chain.set_next(EmailHandler()).set_next(PasswordHandler())

    data_name = data.copy()
    data_name['name'] = ''

    data_email = data.copy()
    data_email['email'] = 'wisderfinyandexru'

    data_password = data.copy()
    data_password['password'] = 'pswrd'

    try:
        chain.handle(data)
        print('OK')
    except Exception as _ex:
        print(_ex)

    try:
        chain.handle(data_name)
    except Exception as _ex:
        print(_ex)

    try:
        chain.handle(data_email)
    except Exception as _ex:
        print(_ex)

    try:
        chain.handle(data_password)
    except Exception as _ex:
        print(_ex)
