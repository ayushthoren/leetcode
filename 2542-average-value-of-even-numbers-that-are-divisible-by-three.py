class Solution:
    def averageValue(self, nums: List[int]) -> int:
        d=[i for i in nums if i%3==0 and i%2==0]
        if d: return sum(d)//len(d)
        return 0
