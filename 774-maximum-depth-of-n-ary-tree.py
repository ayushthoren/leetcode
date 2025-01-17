"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        q,levels=[root],0
        while q:
            new=[]
            levels+=1
            for i in q: new.extend(i.children)
            q=new
        return levels
