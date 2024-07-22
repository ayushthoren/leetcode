# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptA,ptB=headA,headB
        while True:
            if not ptA and not ptB: return None
            if not ptA: ptA=headB
            if not ptB: ptB=headA
            if ptA is ptB: return ptA
            ptA,ptB=ptA.next,ptB.next
