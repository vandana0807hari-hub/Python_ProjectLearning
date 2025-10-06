class Car:
 # Class Variable - belongs to whole class and can be shared among all the objects of a class
    cateogery = "motervehicles"  # defined outside the constructor 
    def __init__(self,brand, color):
 # Insatance Variable - belongs to specific object and has their own value/unique 
        self.brand = brand # defined inside the constructor
        self.color = color

    

# objects
car1 = Car("BMW", "white") 
car2 = Car("Honda", "Silver")
    
print (car1.brand)
print (car1.color)



    


