# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        vals,q=[],[root]
        while q:
            new=[]
            vals.append([])
            for i in q:
                vals[-1].append(i.val)
                if i.left: new.append(i.left)
                if i.right: new.append(i.right)
            q=new
        return vals