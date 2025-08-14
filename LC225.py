#225. Implement Stack using Queues
#https://leetcode.com/problems/implement-stack-using-queues/description/?envType=problem-list-v2&envId=stack


class MyStack:

    def __init__(self):
        self.stack_list = []

    def push(self, x: int) -> None:
        self.stack_list.append(x)

    def pop(self) -> int:
        if self.is_empty():
            return None
        return self.stack_list.pop()

    def is_empty(self) -> bool:
        return len(self.stack_list) == 0

    def top(self) -> int:
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def empty(self) -> bool:
        return self.is_empty()


# Testing the stack operations
operations = ["MyStack", "push", "push", "top", "pop", "empty"]
values = [None, 1, 2, None, None, None]

output = []
stack = None

for op, val in zip(operations, values):
    if op == "MyStack":
        stack = MyStack()
        output.append(None)
    elif op == "push":
        stack.push(val)
        output.append(None)
    elif op == "top":
        output.append(stack.top())
    elif op == "pop":
        output.append(stack.pop())
    elif op == "empty":
        output.append(stack.empty())

print("Output:", output)
