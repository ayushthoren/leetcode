# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q,vals=[root],[]
        while q:
            vals.append([])
            new=[]
            for i in q:
                if i.left: new.append(i.left)
                if i.right: new.append(i.right)
                vals[-1].append(i.val)
            q=new
        return [v[-1] for v in vals]
