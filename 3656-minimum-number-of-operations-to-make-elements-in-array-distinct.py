class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s=defaultdict(bool)
        for i in range(len(nums)-1,-1,-1):
            if s[nums[i]]: return i//3+1
            s[nums[i]]=True
        return 0
