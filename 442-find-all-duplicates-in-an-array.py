class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        o = []
        for n in nums:
            i = abs(n) - 1
            if nums[i] < 0: o.append(i + 1); continue
            nums[i] *= -1
        return o
