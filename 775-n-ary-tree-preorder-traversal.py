"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        stack,vals=[root],[]
        while stack:
            vals.append(stack[-1].val)
            stack.extend(reversed(stack.pop().children))
        return vals
