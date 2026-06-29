# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        q, m = [(root, 0)], 0

        while q:
            l, r = q[0][1], q[-1][1]
            m = max(m, r - l + 1)
            
            t = []
            for n, i in q:
                if n.left: t.append((n.left, i * 2))
                if n.right: t.append((n.right, i * 2 + 1))
            q=t

        return m
