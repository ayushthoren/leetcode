# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1,node=[],l1
        while node:
            n1.append(node.val)
            node=node.next
        n1=int("".join(map(str,n1[::-1])))
        n2,node=[],l2
        while node:
            n2.append(node.val)
            node=node.next
        n2=int("".join(map(str,n2[::-1])))
        n3=str(n1+n2)
        node=None
        for i in n3:
            if not node: node=ListNode(i)
            else:
                node=ListNode(0,node)
                node.val=int(i)
        return node
