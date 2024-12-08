# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q,vals=[root],[]
        while q:
            new,tmp=[],None
            for i in q:
                if i.left: new.append(i.left)
                if i.right: new.append(i.right)
                if tmp==None or i.val>tmp: tmp=i.val
            q=new
            vals.append(tmp)
        return vals
