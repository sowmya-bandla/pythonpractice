import numpy as np 
class Queue:
    def __init__(self):
        self.items=[]
    
    def is_empty(self):
        return self.items==[]
    
    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return 'Queue is empty'
    
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return 'Queue is empty'
    
    def size(self):
        return len(self.items)
    
    def display(self):
        print('Queue:', self.items)

q = Queue()
q.enqueue(5)
q.enqueue(10)
q.enqueue(15)

q.display()            
print(q.dequeue())     
print(q.peek())       
q.display()       