class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n,nums,i=len(nums),[int(x,2) for x in nums],0
        while True:
            if i not in nums:
                o=bin(i)[2:]
                return "0"*(n-len(o))+o
            i+=1
