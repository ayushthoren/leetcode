# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
          if root == None: return
          stack = []

          ptr = root

          while True:
            if ptr is not None:

              if ptr.val==val: return ptr

              stack.append(ptr)
              ptr = ptr.left

            elif len(stack) != 0:
              ptr = stack.pop()
              # print(ptr.val)
              ptr = ptr.right

            else:
              break
