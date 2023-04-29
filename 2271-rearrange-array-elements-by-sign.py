class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p,n=[],[]
        for i in nums:
            if i>0: p.append(i)
            else: n.append(i)
        new=[]
        for j in range(len(nums)):
            if j%2==0:
                new.append(p[0])
                p.pop(0)
            else:
                new.append(n[0])
                n.pop(0)
        return new
