class Node: 
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def printList(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length+=1
        return True  

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:            
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length-=1
        return temp.value   

    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node        
            self.head = new_node      
        self.length +=1
        return True

    def popFirst(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:            
            self.head = temp.next
            self.head.prev = None
            temp.next = None
        self.length-=1
        return temp.value       
    
    def get (self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next    
        else:
            temp = self.tail    
            for _ in range(self.length-1, index, -1):
                temp = temp.prev  
        return temp.value      

         

my_doubly_LL = DoublyLinkedList(7)
# my_doubly_LL.prepend(8)
my_doubly_LL.append(6)
my_doubly_LL.append(5)
my_doubly_LL.printList()
print("The value of the Node at index is:", my_doubly_LL.get(3))
# my_doubly_LL.printList()
# print(my_doubly_LL.popFirst())
# print(my_doubly_LL.popFirst())
# print(my_doubly_LL.popFirst())

# print(my_doubly_LL.popFirst())





# print(my_doubly_LL.pop())
# print(my_doubly_LL.pop())

# print(my_doubly_LL.pop())

         
