"""Stack: Reverse String ( ** Interview Question)
The reverse_string function takes a single parameter string, which is the string you want to reverse.

Return a new string with the letters in reverse order.

This will use the Stack class we created in the last three coding exercises:"""

class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()



def reverse_string(my_string) -> str:
    stack_list = Stack()
    for char in my_string:
        stack_list.push(char)
        
    reversed_str = ''
    while not stack_list.is_empty():
        reversed_str += stack_list.pop()

    return reversed_str    
        
      


my_string = 'hello'

print ( reverse_string(my_string) )


