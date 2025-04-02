class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ln,o=len(nums),0
        for i in range(ln):
            for j in range(i+1,ln):
                for k in range(j+1,ln):
                    o=max((nums[i]-nums[j])*nums[k],o)
        return o
