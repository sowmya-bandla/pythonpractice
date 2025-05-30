import numpy as np 
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class linked_list:
    def __init__(self):
        self.head=None

    def insert_end(self,data):
        new_node=node(data)
        if not self.head:
            self.head=new_node
            return 
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node

    def insert_beginning(self, data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node 

    def delete(self, key):
        current = self.head
        prev = None
        while current:
            if current.data == key:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True  
            prev = current
            current = current.next
        return False  

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


ll = linked_list()
ll.insert_end(10)
ll.insert_end(20)
ll.insert_beginning(5)
ll.display()  

ll.delete(10)
ll.display()  

print("Search 20:", ll.search(20)) 
print("Search 100:", ll.search(100))      
