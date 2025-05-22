#Create a class Student with a method to input and display marks for 3 subjects. Use a list to store marks
class student:
    def __init__(self,name):
        self.name=name
        self.marks=[]
    def input_marks(self):
        print(f"enter the marks for {self.name}:")
        for i in range(3):
            mark=float(input(f"subject {i+1} marks:"))
            self.marks.append(mark)
    
    def display_marks(self):
        print(f"\nmarks for{self.name}:")
        for i, mark in enumerate(self.marks,start=1):
            print(f" subject {i}: {mark}")

std1=student("alice")
std1.input_marks()
std1.display_marks()
      
