#2095. Delete the Middle Node of a Linked List
#https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

class Solution:
    def deleteMiddle(self,head):
        if head is None or head.next is None:
            return None 
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next      
        return head   
          

      



