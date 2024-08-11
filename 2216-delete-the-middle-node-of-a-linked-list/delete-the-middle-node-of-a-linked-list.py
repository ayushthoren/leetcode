# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals=[]
        while head:
            vals.append(head.val)
            head=head.next
        lv=len(vals)
        vals.pop(lv//2)
        new=None
        for i in range(1,lv):
            if not new: new=ListNode(vals[i*-1])
            else: new=ListNode(vals[i*-1],new)
        return new