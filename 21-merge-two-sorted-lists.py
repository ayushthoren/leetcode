# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2: return
        l1,l2=[],[]
        while list1: l1.append(list1.val); list1=list1.next
        while list2: l2.append(list2.val); list2=list2.next
        l3=sorted(l1+l2)[::-1]
        node=ListNode()
        for i in range(len(l3)-1):
            node.val=l3[i]
            node=ListNode(0,node)
        node.val=l3[-1]
        return node
