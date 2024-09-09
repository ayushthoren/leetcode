# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q,sums=[root],[]
        while q:
            sums.append(sum([i.val for i in q]))
            new=[]
            for j in q:
                if j.left: new.append(j.left)
                if j.right: new.append(j.right)
            q=new
        return sums.index(max(sums))+1
