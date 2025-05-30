import numpy as np 
class stack:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return self.items==[]
    
    def push(self,items):
        self.items.append(items)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return 'stack is empty' 
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return 'stack is empty'
    
    def size(self):
        return len(self.items)
    
    def display(self):
        print('stack:', self.items)


s = stack()
s.push(5)
s.push(10)
s.push(15)
s.display()           
print(s.pop())       
print(s.peek()) 
print(s.size())     
s.display() 