class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
        
class Doubly_Linked_List:
    
    def __init__(self):
        
        self.head = None
        
    def insert_at_beg(self,data):
        
        new_node = Node(data)
        new_node.prev = None
        new_node.next = self.head
        
        if self.head is not None:
             self.head.prev = new_node
            
        self.head = new_node
        
        
    def reverse(self):
        current = self.head
        while current.next is not None:
            
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        
        current.next = current.prev
        current.prev = None
        
        self.head = current
        
    def display(self):
        
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
        
        
d1 = Doubly_Linked_List()
d1.insert_at_beg(4)
d1.insert_at_beg(5)
d1.insert_at_beg(6)
d1.insert_at_beg(7)

d1.display()
d1.reverse()
d1.display()