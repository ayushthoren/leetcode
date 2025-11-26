# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        a, b, c, m = head, head, None, 0
        while a: a, b = a.next.next, b.next
        while b: b.next, c, b = c, b, b.next
        while c: m, c, head = max(m, head.val + c.val), c.next, head.next
        return m
