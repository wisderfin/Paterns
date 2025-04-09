from time import sleep

class API:
    def square(self, x: int) -> int:
        sleep(3)
        return x**2

class ProxyAPI:
    def __init__(self, api: API):
        self.api = api
        self._cache = {}

    def square(self, x):
        if x not in self._cache:
            self._cache[x] = self.api.square(x)
        return self._cache[x]


if __name__ == '__main__':
    api = ProxyAPI(API())
    print(api.square(1))
    print(api.square(2))
    print(api.square(1))
    print(api.square(3))
    print(api.square(2))
    print(api.square(1))
