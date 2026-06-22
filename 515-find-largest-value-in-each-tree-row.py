# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q, o = [root], []

        while q:
            n, m = [], None
            for i in q:
                if i.left: n.append(i.left)
                if i.right: n.append(i.right)
                if m == None or i.val > m: m = i.val
            o.append(m)
            q = n

        return o
