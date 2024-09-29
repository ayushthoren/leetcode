class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        return list(set([i for i in nums if nums.count(i)==2]))
