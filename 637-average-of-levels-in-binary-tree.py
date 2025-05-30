# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q,avgs=[root],[]
        while q:
            new,vals=[],[]
            for i in q:
                vals.append(i.val)
                if i.left: new.append(i.left)
                if i.right: new.append(i.right)
            avgs.append(sum(vals)/len(vals))
            q=new
        return avgs
