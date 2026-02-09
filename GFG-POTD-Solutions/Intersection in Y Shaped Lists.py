'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def intersectPoint(self, head1, head2):
        # code here
        p1 , p2 = head1,head2
        while p1 != p2:
            p1=p1.next if p1 else head2
            p2=p2.next if p2 else head1
        return p1