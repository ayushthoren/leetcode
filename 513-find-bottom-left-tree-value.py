# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q=[root]
        while True:
            new=[]
            for i in q:
                if i.left: new.append(i.left)
                if i.right: new.append(i.right)
            if new: q=new
            else: break
        return q[0].val
