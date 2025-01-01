# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q,sums=[root],[]
        while q:
            sums.append(0)
            new=[]
            for i in q:
                if i.left: new.append(i.left)
                if i.right: new.append(i.right)
                sums[-1]+=i.val
            q=new
        try: return sorted(sums,reverse=True)[k-1]
        except: return -1
