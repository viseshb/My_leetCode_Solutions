#232. Implement Queue using Stacks
#https://leetcode.com/problems/implement-queue-using-stacks/description/?envType=problem-list-v2&envId=stack

class MyQueue:

    def __init__(self):
        self.queue_list = []

    def push(self, x: int) -> None:
        self.queue_list.append(x)

    def pop(self) -> int:
        if self.is_empty():
            return None
        return self.queue_list.pop(0)

    def is_empty(self):
        return len(self.queue_list) == 0

    def peek(self) -> int:
        if self.is_empty():
            return None
        return self.queue_list[0]

    def empty(self) -> bool:
        return self.is_empty()


# Simulate the operations
operations = ["MyQueue", "push", "push", "peek", "pop", "empty"]
values = [None, 1, 2, None, None, None]

output = []
queue = None

for op, val in zip(operations, values):
    if op == "MyQueue":
        queue = MyQueue()
        output.append(None)
    elif op == "push":
        queue.push(val)
        output.append(None)
    elif op == "peek":
        output.append(queue.peek())
    elif op == "pop":
        output.append(queue.pop())
    elif op == "empty":
        output.append(queue.empty())

print("Output:", output)
