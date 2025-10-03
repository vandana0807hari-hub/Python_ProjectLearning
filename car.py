class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def drive(self):
        print("car is driving")

car1 = Car("Toyota", 2022)
car2 = Car("Honda", 2023)

print(car1.brand)
print(car1.year)
car1.drive()