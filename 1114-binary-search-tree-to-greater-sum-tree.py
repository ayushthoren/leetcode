# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        q,vals=[root],[]
        while q:
            new=[]
            for i in q:
                if i.left: new.append(i.left)
                if i.right: new.append(i.right)
                vals.append(i.val)
            q=new
        vals.reverse()
        q=[root]
        while q:
            new=[]
            for j in q:
                j.val+=sum(v for v in vals if v>j.val)
                if j.left: new.append(j.left)
                if j.right: new.append(j.right)
            q=new
        return root
