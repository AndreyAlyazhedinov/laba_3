class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value=None):
        if not hasattr(self, "value"):
            self.value = value


if __name__ == "__main__":
    first = Singleton("начальное значение")
    second = Singleton("это значение будет проигнорировано")
    print(first is second)
    print(first.value, second.value)
