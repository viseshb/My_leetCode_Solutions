#1290. Convert Binary Number in a Linked List to Integer
#https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        num = 0
        current = head

        while current:
            num = num*2 + current.val
            current = current.next
        return num    
        