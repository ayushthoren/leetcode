# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals,tmp,merges=[],[],[]
        while head:
            vals.append(head.val)
            head=head.next
        for i in vals[1:]:
            if i==0: merges.append(sum(tmp)); tmp=[]
            else: tmp.append(i)
        merges.reverse()
        newHead=ListNode(merges[0])
        for j in merges[1:]: newHead=ListNode(j,newHead)
        return newHead
