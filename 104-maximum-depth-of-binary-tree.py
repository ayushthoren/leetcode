# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        q,m=[root],0
        while q:
            m+=1
            new=[]
            for i in q:
                if i.left: new.append(i.left)
                if i.right: new.append(i.right)
            q=new
        return m
