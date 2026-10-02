class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        print("Какой-то звук")

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} - Гав!")
    def fetch(self):
        print(f"{self.name} - приносит палку")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} - Мяу!")
    def scratch(self):
        print(f"{self.name} - царапает диван")

dog = Dog("Бобик")
cat = Cat("Мурка")

dog.make_sound()
dog.fetch()

cat.make_sound()
cat.scratch()

animals = [Dog("Шарик"), Cat("Барсик"), Dog("Рекс")]

for animal in animals:
    animal.make_sound()