# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head,tmp,merges=head.next,[],[]
        while head:
            tmp.append(head.val)
            if head.val==0: merges.append(sum(tmp)); tmp=[]
            head=head.next
        merges.reverse()
        newHead=ListNode(merges[0])
        for j in merges[1:]: newHead=ListNode(j,newHead)
        return newHead
