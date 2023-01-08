class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return [i for i in nums if i%2==0]+[j for j in nums if j%2==1]
