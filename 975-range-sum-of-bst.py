# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        q,vals=[root],[]
        while q:
            new=[]
            for i in q:
                vals.append(i.val)
                if i.left: new.append(i.left)
                if i.right: new.append(i.right)
            q=new
        return sum(j for j in vals if low<=j<=high)
