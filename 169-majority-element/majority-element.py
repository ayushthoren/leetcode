class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numsl=len(nums)/2
        cts={}
        for i in nums:
            if i not in cts: cts[i]=nums.count(i)
            if cts[i]>numsl: return i