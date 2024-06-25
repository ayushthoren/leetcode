class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        out,ln,found=[-1,-1],len(nums),False
        for i in range(ln):
            if nums[i]==target:
                if found: out[1]=i
                else:
                    out[0]=i
                    if i==ln-1: out[1]=i
                    found=True
            if found and nums[i]!=target: out[1]=i-1; found=False
        return out
