#https://leetcode.com/problems/add-two-numbers/description/?envType=problem-list-v2&envId=linked-list
#2. Add Two Numbers 
#You are given two non-empty linked lists representing two non-negative integers.
#  The digits are stored in reverse order, and each of their nodes contains a single digit.
#  Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

class Solution:
    def addTwoNumbers(self, l1: Node, l2: Node) -> Node:
        dummy = Node(0) 
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.value if l1 else 0
            val2 = l2.value if l2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10

            current.next = Node(total % 10)  
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next  


def create_linked_list(lst):
    linked_list = LinkedList()
    for number in lst:
        linked_list.append(number)
    return linked_list.head  


def print_linked_list(head):
    nums = []
    while head:
        nums.append(str(head.value))
        head = head.next
    print(" -> ".join(nums))


l1 = create_linked_list([5, 6, 4, 3])  
l2 = create_linked_list([2, 5, 7])    
solution = Solution()
result = solution.addTwoNumbers(l1, l2)

print("Output linked list:")
print_linked_list(result)  
