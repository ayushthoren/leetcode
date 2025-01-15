# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(root):
            q,vals=[root],[]
            while q:
                new=[]
                vals.append([])
                for i in q:
                    if i:
                        vals[-1].append(i.val)
                        new.append(i.left)
                        new.append(i.right)
                    else: vals[-1].append(None)
                q=new
            return vals
        return traverse(p)==traverse(q)
