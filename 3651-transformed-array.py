class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        ln,result=len(nums),[0 for i in nums]
        def getIdx(start,amt,right):
            step = 1 if right else -1
            for i in range(0,amt):
                start += step
                if start < 0: start = ln-1
                elif start > ln-1: start = 0
            return start
        for i in range(ln):
            if nums[i] > 0: result[i] = nums[getIdx(i,nums[i],True)]
            if nums[i] < 0: result[i] = nums[getIdx(i,abs(nums[i]),False)]
            if nums[i] == 0: result[i] = nums[i]
        return result
