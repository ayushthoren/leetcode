class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        summ=0
        for i in range(k): summ+=max(nums)+i
        return summ
