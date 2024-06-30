# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        vals,q=[],[root]
        while q:
            new=[]
            for i in q:
                vals.append(i.val)
                if i.left: new.append(i.left)
                if i.right: new.append(i.right)
            q=new
        m=None
        for j in range(len(vals)):
            for k in range(len(vals)):
                if j!=k and (not m or abs(vals[j]-vals[k])<m): m=abs(vals[j]-vals[k])
        return m
