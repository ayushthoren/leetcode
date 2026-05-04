class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        p1, p2 = 0, len(nums)-1
        l, r = 0, 0
        o = set()
        while p2 >= 0:
            if nums[p1] > l: l = nums[p1]; o.add(p1)
            if nums[p2] > r: r = nums[p2]; o.add(p2)
            p1 += 1; p2 -= 1
        return [nums[i] for i in sorted(list(o))]
