# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helperInorder(self, root: Optional[TreeNode], arr) -> List[int]:
      if root==None: return
      self.helperInorder(root.left, arr)
      arr.append(root.val)
      self.helperInorder(root.right, arr)
      return arr

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      if root == None: return []
      return self.helperInorder(root, [])
