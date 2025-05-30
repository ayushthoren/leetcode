class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum((math.floor(math.log10(i))+1)%2==0 for i in nums)
