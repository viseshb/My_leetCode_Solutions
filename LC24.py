#24. Swap Nodes in Pairs
#https://leetcode.com/problems/swap-nodes-in-pairs/description/?search=swap+ad&page=1


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Solution:
    def swapAdjacentNodes(self, head: Node)-> Node:
        dummy = Node(0)
        dummy.next = head  
        current = dummy

        while current.next and current.next.next:
            first = current.next
            second = current.next.next

            first.next = second.next
            second.next = first
            current.next = second
            current = first 

        return dummy.next
              