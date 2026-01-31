# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        v = []
        def inorder(n):
            if n == None: return
            inorder(n.left)
            v.append(n.val)
            inorder(n.right)
        inorder(root)
        return min(v[i]-v[i-1] for i in range(1, len(v)))
