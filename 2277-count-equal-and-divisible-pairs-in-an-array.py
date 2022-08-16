class Solution(object):
    def countPairs(self, nums, k):
      ct=0
      pairs=[]
      for i in range(len(nums)):
        for j in range(len(nums)):
          if i!=j and [j,i] not in pairs:
            if nums[i]==nums[j] and (i*j)%k==0: ct+=1; pairs.append([i,j])
      return ct
