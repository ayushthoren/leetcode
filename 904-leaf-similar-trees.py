# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(n, v):
            if not n: return
            if not n.left and not n.right: v.append(n.val)
            dfs(n.left, v); dfs(n.right, v)
        a, b = [], []
        dfs(root1, a); dfs(root2, b)
        return a == b
