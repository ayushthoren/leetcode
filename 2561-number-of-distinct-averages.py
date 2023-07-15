class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        p1,p2=0,len(nums)-1
        nums,avg=sorted(nums),[]
        while p1<p2:
            avg.append((nums[p1]+nums[p2])/2)
            p1+=1
            p2-=1
        return len(set(avg))
