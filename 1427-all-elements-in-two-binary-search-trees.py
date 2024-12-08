# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def getVals(root):
            if not root: return []
            q,vals=[root],[]
            while q:
                new=[]
                for i in q:
                    if i.left: new.append(i.left)
                    if i.right: new.append(i.right)
                    vals.append(i.val)
                q=new
            return vals
        return sorted(getVals(root1)+getVals(root2))
