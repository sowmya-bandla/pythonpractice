class Employee:
    #Constructor
    def __init__(self,empno,empname,salary):
        self.empno=empno
        self.empname=empname
        self.salary=salary
   
    def display(self):
        
        print("   empno ",self.empno)
        print("   empno ",self.empname)
        print("   empno ",self.salary)
        
        print(f" Hello My naame is {self.empname} and my salary is {self.salary}")
        #print(self)
 
emp1=Employee(101,"Nageswara",1000)
 
emp1.display()
 
print(emp1.empname)
emp1.empname="Raju"
print(emp1.empname)