# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        q,ct=[root],0
        while q:
            new=[]
            for i in q:
                if i.left: new.append(i.left)
                if i.right: new.append(i.right)
                ct+=1
            q=new
        return ct