# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helperPreorder(self, root: Optional[TreeNode], arr) -> List[int]:
      if root==None: return
      arr.append(root.val)
      self.helperPreorder(root.left, arr)
      self.helperPreorder(root.right, arr)
      return arr

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      if root == None: return []
      return self.helperPreorder(root, [])
