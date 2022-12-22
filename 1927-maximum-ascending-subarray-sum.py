class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        numsl=len(nums)
        asc=[]
        for i in range(numsl+1):
            for j in range(i,numsl+1):
                sub=nums[i:j]
                if sub==sorted(sub) and len(set(sub))==len(sub): asc.append(sub)
        print(asc)
        if asc: return max([sum(k) for k in asc])
        else: return max(nums)
