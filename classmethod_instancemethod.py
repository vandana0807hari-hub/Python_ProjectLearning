class Car:
    wheels = 4

    def __init__(self, brand):
        self.brand = brand

#Instance Method
    def change_brand(self,new_brand):
        self.brand = new_brand

#Class Method
    @classmethod
    def change_wheels(cls,new_count):
        cls.wheels = new_count

#Objects
car1 = Car("BMW")
car2 = Car("Honda")

# Using instance method we can modify instance variable brand from BMW to Porsche and Honda to Audi
car1.change_brand ("Porsche")
car2.change_brand ("Audi")

# Using class method we can change wheels count from 4 to 6
Car.change_wheels (6)


print (car1.change_brand)
print (car1.change_wheels)