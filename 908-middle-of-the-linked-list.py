# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def ll_len(ll):
  ptr, size = ll, 0
  while ptr:
    ptr = ptr.next
    size += 1
  return size

class Solution:
        def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
          length=ll_len(head)
          if length%2==0: length=(length//2)
          else: length=length//2

          ptr=head
          for i in range(length): ptr=ptr.next
          return ptr
