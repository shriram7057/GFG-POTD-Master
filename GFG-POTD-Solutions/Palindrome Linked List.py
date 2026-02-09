'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def isPalindrome(self, head):
        # code here
        if not head or not head.next:
            return True
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast=fast.next.next
        prev=None
        while slow:
            nxt = slow.next
            slow.next=prev
            prev=slow
            slow=nxt
        left = head
        right=prev
        while right:
            if left.data != right.data:
                return False
            left = left.next
            right = right.next
        return True
        