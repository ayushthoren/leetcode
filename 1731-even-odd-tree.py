# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        levels,q=[],[root]
        while q:
            vals,new=[],[]
            for i in q: 
                vals.append(i.val)
                if i.left: new.append(i.left)
                if i.right: new.append(i.right)
            levels.append(vals)
            q=new
        e=True
        for j in levels:
            if e:
                for k in j:
                    if k%2!=1: print("even at even"); return False
                if sorted(set(j))!=j: print("not increasing at even"); return False
            else:
                for l in j:
                    if l%2!=0: print("odd at odd"); return False
                if sorted(set(j),reverse=True)!=j: print("not decreasing at odd"); return False
            e=not e
            print(e)
        return True
