# Defining the Class Car
class Car :
    def __init__(self, model , color ) :
        self.model = model
        self.color = color

    def displayCar(self) :
        print(self.color, self.model)
        
    def descriptionCar(self) : 
        return (self.color + " " + self.model)

# Lets start using the Class

car1 = Car("Tesla", "Red")
car1.displayCar()

car2 = Car("Ford", "Black")
print(car2.model)
print(car2.color)

car3 = Car("Pontiac", "Blue")
print(car3.model)
print(car3.color)

car3.color = "Grey"
car3.displayCar()
print(car3.descriptionCar())
