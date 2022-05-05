# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
      if root == None: return
      stack = []

      ptr = root

      vals=[]

      while True:
        if ptr is not None:
          stack.append(ptr)
          ptr = ptr.left

        elif len(stack) != 0:
          ptr = stack.pop()
          vals.append(ptr.val)
          ptr = ptr.right

        else:
          break

      cts=[vals.count(j) for j in vals]
      return list(set([i for i in vals if vals.count(i)==max(cts)]))
