class ListNode:
    def __init__(self,value):
        self.value = value
        self.next= None


def reverse(self, head: ListNode):
    prev = None
    current = head
    while current:
        after = current.next
        current.next = prev
        prev= current
        current = after
    return prev
    


def isPalindrome(self, head: ListNode):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    rev = self.reverse(slow)
    while rev:
        if head.val != rev.value:
            return False
        head = head.next
        rev = rev.next
    return True    
