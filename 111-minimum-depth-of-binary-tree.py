# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        d,q=0,[root]
        while True:
            d+=1
            new=[]
            for i in q:
                if not i.left and not i.right: return d
                if i.left: new.append(i.left)
                if i.right: new.append(i.right)
            q=new
