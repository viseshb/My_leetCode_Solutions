#https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=problem-list-v2&envId=linked-list
#19. Remove Nth Node From End of List
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length =1 


class Solution:
    def removeNthFromEnd(self, head: Node, n):
        dummy = Node(0,head)
        slow = dummy
        fast = head

        while n>0 and fast is not None:
            fast = fast.next
            n-=1

        if n>0:
            return None    

        while fast is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next     