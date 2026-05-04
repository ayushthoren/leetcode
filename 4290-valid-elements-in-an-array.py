class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        l, r = 0, 0
        lr, rl = [], []
        for i in range(len(nums)):
            lr.append(l); rl.append(r)
            if nums[i] > l: l = nums[i]
            if nums[-(i+1)] > r: r = nums[-(i+1)]
        rl.reverse()
        return [nums[n] for n in range(len(nums)) if nums[n] > lr[n] or nums[n] > rl[n]]
