class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def reverseDLL(self):
        current = self.head
        new_head = None  # This will eventually be the new head after reversal.

        while current:
            # Save the next pointer before swapping.
            temp = current.next

            # Swap next and prev pointers for the current node.
            current.next = current.prev
            current.prev = temp           
            new_head = current           
            current = temp        
        self.tail = self.head
        self.head = new_head
        return self.head

# Testing the implementation:
my_DLL = DoubleLinkedList(1)
my_DLL.append(5)
my_DLL.append(6)
print('DLL before reverse():')
my_DLL.print_list()

my_DLL.reverseDLL()

print('DLL after reverse():')
my_DLL.print_list()
