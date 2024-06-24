# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or not any(lists): return
        l=[]
        for j in lists:
            while j: l.append(j.val); j=j.next
        l=sorted(l)[::-1]
        node=ListNode()
        for i in range(len(l)-1):
            node.val=l[i]
            node=ListNode(0,node)
        node.val=l[-1]
        return node
