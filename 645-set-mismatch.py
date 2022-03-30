class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        cts={}
        nums.sort()
        for i in range(1, len(nums)+1):
            j=nums[i-1]
            if j not in cts: cts[j]=0
            cts[j]+=1
            if cts[j]>1: d=j
            if i not in cts: n=i
        return [d,n]
