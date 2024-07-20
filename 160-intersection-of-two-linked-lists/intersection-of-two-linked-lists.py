# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        stackA,stackB=[],[]
        while headA:
            stackA.append(headA)
            headA=headA.next
        while headB:
            stackB.append(headB)
            headB=headB.next
        last=None
        while stackA and stackB:
            if stackA[-1] is stackB[-1]:
                last=stackA.pop(-1)
                stackB.pop(-1)
            else: return last
        return last
