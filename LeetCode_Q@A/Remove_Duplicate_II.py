#82. Remove Duplicates from Sorted List II
#https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

class ListNode:
     def __init__(self,val):
          self.val = val
          self.next = None

class LinkedList:
     def __init__(self,val):
           new_node = ListNode(val)
           self.head = new_node
           self.tail = new_node
           self.length = 1
     


class Solution:
    def deleteDuplicates(self, head: ListNode)-> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        previous = dummy
        current = head

        while current:
             duplicate = False
             while current and current.val == current.next.val:
                  duplicate = True
                  current = current.next

             if duplicate:
                  previous.next = current.next
             else:
                  previous = current
             current = current.next

        head = dummy.next
        return head     


