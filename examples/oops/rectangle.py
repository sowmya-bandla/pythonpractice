#Create a class Rectangle with methods to calculate area and perimeter. Take length and breadth as inputs during object creation.
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    
    def perimeter(self):
        return 2*(self.length+self.breadth)
    

rect1=Rectangle(10,3)
print("Area:", rect1.area())
print("Perimeter:", rect1.perimeter())
