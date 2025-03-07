# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ans=ListNode(next=head)
        p=ans
        for _ in range(n): head=head.next
        while head: head,p=head.next,p.next
        p.next=p.next.next
        return ans.next
