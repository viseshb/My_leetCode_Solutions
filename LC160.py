#160. Intersection of Two Linked Lists
#https://leetcode.com/problems/intersection-of-two-linked-lists/description/?envType=problem-list-v2&envId=linked-list

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def intersectionOfTwoLinkedList(self, headA, headB):
    current1 = headA
    current2 = headB

    while current1 is not current2:
        current1 = current1.next if current1 else headB
        current2 = current2.next if current2 else headA
    return current1


