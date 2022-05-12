# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helperPostorder(self, root: Optional[TreeNode], arr) -> List[int]:
      if root==None: return
      self.helperPostorder(root.left, arr)
      self.helperPostorder(root.right, arr)
      arr.append(root.val)
      return arr

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      if root == None: return []
      return self.helperPostorder(root, [])
