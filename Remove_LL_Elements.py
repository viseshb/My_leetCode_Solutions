#203. Remove Linked List Elements
#https://leetcode.com/problems/remove-linked-list-elements/description/?envType=problem-list-v2&envId=linked-list

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

class Solution:
    def removeLLElements(self, head, val):
        dummy = Node(0)
        dummy.next = head
        prev = dummy
        current = head

        while current:
            if current.value == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        return dummy.next                            