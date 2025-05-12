#92. Reverse Linked List II
#https://leetcode.com/problems/reverse-linked-list-ii/description/


#Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy        

        for _ in range(left -1):
            prev = prev.next
        current = prev.next    

        for _ in range(right - left):
            after = current.next
            current.next = after.next
            after.next = prev.next
            prev.next = after 

        return dummy.next             
        