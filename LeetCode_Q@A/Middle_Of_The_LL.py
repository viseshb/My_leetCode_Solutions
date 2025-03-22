#876. Middle of the Linked List
#https://leetcode.com/problems/middle-of-the-linked-list/description/

class Solution:
    def middleNode(self):
      slow = self.head
      fast = self.head

      while fast and fast.next:
          slow = slow.next
          fast = fast.next.next
      return slow



