class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        o, e = 0, 0
        a = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            if nums[i] % 2 == 1: a[i] = e; o += 1
            else: a[i] = o; e += 1
        return a
