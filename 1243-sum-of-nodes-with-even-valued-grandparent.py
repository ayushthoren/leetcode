# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        root.parent = None
        q, v = [root], []
        while q:
            new = []
            for i in q:
                if i.parent and i.parent.parent and i.parent.parent.val % 2 == 0: v.append(i.val)
                if i.left: i.left.parent = i; new.append(i.left)
                if i.right: i.right.parent = i; new.append(i.right)
            q = new
        return sum(v)
