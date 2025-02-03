# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return
        q,level=[root],0
        while q:
            ln=2**level
            current,q=q,[]
            for i in current:
                if i.left: q.append(i.left)
                if i.right: q.append(i.right)
            if level%2==1:
                p1,p2=0,ln-1
                while p1<p2:
                    current[p1].val,current[p2].val=current[p2].val,current[p1].val
                    p1+=1
                    p2-=1
            level+=1
        return root
