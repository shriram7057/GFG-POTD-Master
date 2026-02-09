'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def addTwoLists(self, head1, head2):
        # code here
        def reverse(head):
            prev = None
            while head:
                nxt=head.next
                head.next=prev
                prev = head
                head = nxt
            return prev
        head1 = reverse(head1)
        head2 = reverse(head2)
        
        carry = 0
        dummy = Node(0)
        cur = dummy
        
        while head1 or head2 or carry:
            s = carry
            if head1:
                s += head1.data
                head1 = head1.next
            if head2:
                s += head2.data
                head2 = head2.next
            carry = s // 10
            cur.next = Node(s % 10)
            cur = cur.next
        res = reverse(dummy.next)
        while res and res.data == 0 and res.next:
            res = res.next
        return res