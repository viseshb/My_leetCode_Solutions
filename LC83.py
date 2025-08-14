#83. Remove Duplicates from Sorted List
#https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
from typing import Optional
class ListNode: 
    def __init__(self,value):
        self.value = value
        self.next = None

class NodeList:
    def __init__(self,value):
        self.head = ListNode
        self.tail = ListNode
        self.length = 1



class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return 
        
        seen = set()
        current = head
        seen.add(current.value)

        while current and current.next:
            if current.next.val in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.val)
                current = current.next
        return head            


        