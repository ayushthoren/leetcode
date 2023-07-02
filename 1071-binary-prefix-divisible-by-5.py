class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        nums,out=[str(n) for n in nums],[]
        for i in range(len(nums)):
            b="0b"+"".join(nums[0:i+1])
            if int(b,2)%5==0: out.append(True)
            else: out.append(False)
        return out
