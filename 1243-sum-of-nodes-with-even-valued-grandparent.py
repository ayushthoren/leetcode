# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        q, s = deque([(root, False, False)]), 0
        while q:
            n, pe, ge = q.popleft()
            if ge: s += n.val
            e = n.val % 2 == 0
            if n.left: q.append((n.left, e, pe))
            if n.right: q.append((n.right, e, pe))
        return s
