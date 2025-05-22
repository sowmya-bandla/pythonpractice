#Create a class Person that has a private attribute __age. Add getter and setter methods using @property.
class person:
    def __init__(self,age):
        self.__age=age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        if value>0:
            self.__age=value
        else:
            print("Invalid age")

p1=person(25)
print(p1.age)

p1.age=30
print(p1.age)

p1.age=-5
