# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        q,s=[root],root.val
        while q:
            new=[]
            for i in q:
                if i.val!=s: return False
                if i.left: new.append(i.left)
                if i.right: new.append(i.right)
            q=new
        return True
