class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError


class Dog(Animal):
    def speak(self):
        return f"{self.name} говорит Гав!"


if __name__ == "__main__":
    dog = Dog("Шарик")
    print(dog.speak())
