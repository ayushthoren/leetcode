class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ln=len(nums)
        new=[None]*ln
        p1,p2,l,r=0,ln-1,0,ln-1
        while p2>=0:
            if nums[p1]<pivot: new[l]=nums[p1]; l+=1
            if nums[p2]>pivot: new[r]=nums[p2]; r-=1
            p1+=1; p2-=1
        return [i if i!=None else pivot for i in new]
