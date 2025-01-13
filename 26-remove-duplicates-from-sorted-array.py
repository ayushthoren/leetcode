class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        found,i,ln=[],0,len(nums)
        while i<ln:
            if nums[i] not in found: found.append(nums[i]); i+=1
            else: nums.pop(i); ln-=1
        return ln
