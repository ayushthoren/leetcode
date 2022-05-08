# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
      if root == None: return
      stack = []
      nodes=[]

      ptr = root

      while True:
        if ptr is not None:
          stack.append(ptr)
          ptr = ptr.left

        elif len(stack) != 0:
          ptr = stack.pop()
          nodes.append(ptr.val)
          ptr = ptr.right

        else:
          break

      if len(set(nodes))>=2: return sorted(list(set(nodes)))[1]
      return -1
