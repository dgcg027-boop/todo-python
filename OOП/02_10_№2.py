class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def info(self):
        print(f"{self.brand} ({self.year})")

class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors
    def info(self):
        print(f"Машина: {self.brand} ({self.year}), дверей: {self.doors}")

class Motorcycle(Vehicle):
    def __init__(self, brand, year, type):
        super().__init__(brand, year)
        self.type = type
    def info(self):
        print(f"Мотоцикл: {self.brand} ({self.year}), тип: {self.type}")
    
car = Car("Toyota", 2020, 4)
moto = Motorcycle("Yamaha", 2022, "спорт")

car.info()
moto.info()

car2 = Car("BMW", 2023, 2)
moto2 = Motorcycle("Harley-Davidson", 2021, "круизер")

car2.info()
moto2.info()

vehicles = [Car("BMW", 2023, 2), Motorcycle("Harley", 2021, "круизер"), Car("Kia", 2019, 4)]

for v in vehicles:
    v.info()