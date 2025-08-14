#206 Reverse Linked list
#https://leetcode.com/problems/reverse-linked-list/

def reverseLL(self):
    before = None
    current = self.head

    while current:
        after = current.next
        current.next = before
        before = current
        current = after

    return before    