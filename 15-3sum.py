class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums, a = sorted(nums), set()
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0: a.add((nums[i], nums[j], nums[k])); j += 1
                elif s < 0: j += 1
                else: k -= 1
        return [list(l) for l in a]
