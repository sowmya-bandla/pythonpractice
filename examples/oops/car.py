
#Create a class Car with attributes brand, model, and year. Add a method to display the car's details.

class car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def display(self):
        print(f"car: {self.brand} {self.model} {self.year}\n")
#test
c1=car("Toyota", "abc", 2010)
c2=car("honda", "erf", 2012)
c1.display()
c2.display()



    





