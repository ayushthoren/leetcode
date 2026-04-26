# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b: a, b = b, a % b
            return a
        i, j = head, head.next
        while j:
            t = ListNode(gcd(i.val, j.val))
            i.next = t; t.next = j
            i, j = j, j.next
        return head
