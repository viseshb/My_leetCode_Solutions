#https://leetcode.com/problems/merge-two-sorted-lists/?envType=problem-list-v2&envId=linked-list
#21. Merge Two Sorted Lists

class Node:
     def __init__(self,value):
          self.value =value
          self.next = next

class LinkedList:
     def __init__(self,value):
          new_node = Node(value)
          self.head = new_node
          self.tail = new_node
          self.length =1 

class Solution:
    def mergeTwoSortedLists(self, l1: Node, l2: Node) ->Node:
            dummy = Node(0)
            current = dummy

            while l1 and l2:
                if l1.value < l2.value:
                   current.next = l1
                   l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next

            if l1:
                 current.next = l1
            elif l2:
                 current.next = l2

            return dummy.next     


                        

              
         
