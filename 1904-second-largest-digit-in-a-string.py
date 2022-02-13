class Solution:
    def secondHighest(self, s: str) -> int:
      #Get all of the unique numbers in the string
      nums=list(set([i for i in s if i.isnumeric()]))
      print(nums)
      #Sort the list
      nums.sort()
      nums=nums[::-1]
      #If the list is longer than 2 elements, return the second largest one
      if len(nums)>1: return nums[1]
      #If there is no second largest digit, return -1
      return -1
