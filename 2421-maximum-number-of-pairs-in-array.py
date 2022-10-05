class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
      pairs=0
      while len(set(nums))!=len(nums):
        rmv=[]
        for i in nums:
          if nums.count(i)>=2 and i not in rmv:
            rmv.append(i)
            pairs+=1
        for j in rmv:
          nums.remove(j)
          nums.remove(j)
      return [pairs, len(nums)]
