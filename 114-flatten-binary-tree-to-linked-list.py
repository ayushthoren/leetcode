# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        q = []
        def p(n):
            if not n: return
            q.append(n)
            p(n.left); p(n.right)
        p(root)

        if q: q.pop(0)
        while q:
            root.right, root.left = q.pop(0), None
            root = root.right
