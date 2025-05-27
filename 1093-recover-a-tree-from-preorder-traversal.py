# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        s,i=[],0
        while i<len(traversal):
            d,v=0,0
            while i<len(traversal) and traversal[i]=="-": d+=1; i+=1
            while i<len(traversal) and traversal[i]!="-": v=v*10+int(traversal[i]); i+=1
            while len(s)>d: s.pop()
            n=TreeNode(v)
            if s:
                if s[-1].left: s[-1].right=n
                else: s[-1].left=n
            s.append(n)
        return s[0]
