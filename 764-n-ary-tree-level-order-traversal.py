"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        q,vals=[root],[]
        while q:
            new=[]
            vals.append([])
            for i in q: vals[-1].append(i.val); new.extend(i.children)
            q=new
        return vals
