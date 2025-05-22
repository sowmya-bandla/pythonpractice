class Student:
    #Class level variables
    schoolName="Govt High School";
 
        # Instance variables
    def __init__(self,stname,classtostudy):
        self.stname=stname
        self.classtostudy=classtostudy
     
 
 
 
s1=Student("Nagesh","A")
print("Studnet Name ",s1.stname)
print("Student 1 School Name ", s1.__class__.schoolName)
print("Class Into ",s1.classtostudy)
 
print("================================")
s2=Student("Ramesh","B")
 
print("Studnet Name ",s2.stname)
print("Student 1 School Name ", s2.__class__.schoolName)
print("Class Into ",s2.classtostudy)