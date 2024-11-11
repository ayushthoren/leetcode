# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def reverse(node):
            if not node: return None
            return TreeNode(node.val,reverse(node.right),reverse(node.left))
        def vals(node):
            q,out=[node],[]
            while q:
                new=[]
                out.append([])
                for i in q:
                    if i:
                        out[-1].append(i.val)
                        if i.left: new.append(i.left)
                        else: new.append(None)
                        if i.right: new.append(i.right)
                        else: new.append(None)
                    else: out[-1].append(None)
                q=new
            return out
        print(vals(root.left),vals(reverse(root.right)))
        return vals(root.left)==vals(reverse(root.right))
