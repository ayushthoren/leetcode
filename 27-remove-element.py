class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        for n in range(len(nums)):
            if nums[n] != val: nums[i] = nums[n]; i+=1
        return i
