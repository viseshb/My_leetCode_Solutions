class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def printList(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
           

    def printListLastNode(self):
        current = self.head
        while current.next:
            current = current.next
        right = current.value
        return right
            
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length +=1
        return True        
    

my_DLL = LinkedList(1)
my_DLL.append(5)
my_DLL.append(6)
print("LL:")
my_DLL.printList()


print("Last Node:", my_DLL.printListLastNode())

