#https://leetcode.com/problems/sort-list/?envType=problem-list-v2&envId=linked-list
#148. Sort List


class ListNode:
    def __init__(self,value):
        self.value = value
        self.next = None

class Solution:
    def sortList(self, head: ListNode):
        if not head or not head.next:
            return head
        
        mid = self.getMid(head)

        prev = None
        current = head

        while current != mid:
            prev = current
            current = current.next

        if prev:
            prev.next = None    

        left_sorted = self.sortList(head)
        right_sorted = self.sortList(mid)
        return self.mergelist(left_sorted, right_sorted)

    def getMid(self, head: ListNode)-> ListNode:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def mergelist(self, l1: ListNode, l2: ListNode) -> ListNode:

        dummy = ListNode(0)
        current = dummy

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next =l2
                l2 = l2.next
            current = current.next


        if l1: 
            current.next = l1
        elif l2 :
            current.next = l2

        return dummy.next                    



    