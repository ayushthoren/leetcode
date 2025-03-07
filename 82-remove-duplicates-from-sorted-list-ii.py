# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans=ListNode(next=head)
        p=ans
        while head:
            while head.next and head.val==head.next.val: head=head.next
            if p.next==head: p=p.next
            else: p.next=head.next
            head=head.next
        return ans.next
