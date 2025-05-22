class Animal():
    def speak(self):
        print("Some sound")

class Cat(Animal):
    def speak(self):
        print("Meow")

c = Cat()
c.speak()

#polymorphisam
class Bird:
    def sound(self):
        print("Some bird sound")

class Sparrow(Bird):
    def sound(self):
        print("Chirp")

class Parrot(Bird):
    def sound(self):
        print("Squawk")

for bird in [Sparrow(), Parrot()]:
    bird.sound()

#static method
class Counter:
    count = 0  # class variable

    @staticmethod
    def increment():
        Counter.count += 1
        print(f"Current count: {Counter.count}")

Counter.increment()
Counter.increment()

#Using __str__ for Better Object Output
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"{self.brand} {self.model}"

car1 = Car("Toyota", "Camry")
print(car1)

#Multiple Inheritance
class A:
    def feature(self):
        print("Feature A")

class B:
    def feature(self):
        print("Feature B")

class C(A, B):
    pass

obj = C()
obj.feature()   # Will call A's feature due to MRO


#Property Decorator for Getter and Setter
class Student:
    def __init__(self):
        self._marks = 0

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if value < 0:
            print("Invalid marks")
        else:
            self._marks = value

s = Student()
s.marks = 85
print(s.marks)