#86. Partition List
#https://leetcode.com/problems/partition-list/description/


#Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1, dummy2 = ListNode(0), ListNode(0)
        ltail,  rtail = dummy1, dummy2
        if not head:
            return None

        while head:
            if head.val < x:
                ltail.next = head
                ltail = ltail.next
            else:
                rtail.next = head
                rtail = rtail.next
            head = head.next

        ltail.next = dummy2.next
        rtail.next = None

        return dummy1.next            

        