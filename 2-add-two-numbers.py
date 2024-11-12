# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getNum(head):
            n=""
            while head:
                n+=str(head.val)
                head=head.next
            return int(n[::-1])
        new=str(getNum(l1)+getNum(l2))
        out=ListNode(int(new[0]))
        for i in new[1:]: out=ListNode(int(i),out)
        return out
