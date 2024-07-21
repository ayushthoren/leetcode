# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue,vals=[root],[]
        while queue:
            tmp,vals=[],[]
            for i in queue:
                vals.append(i.val)
                if i.left: tmp.append(i.left)
                if i.right: tmp.append(i.right)
            queue=tmp
        return sum(vals)
