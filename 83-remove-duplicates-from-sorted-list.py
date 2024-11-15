# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        vals=[]
        while head:
            vals.append(head.val)
            head=head.next
        vals=sorted(list(set(vals)))[::-1]
        new=ListNode(vals[0])
        for i in vals[1:]: new=ListNode(i,new)
        return new
