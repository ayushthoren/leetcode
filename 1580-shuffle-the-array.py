class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
      n1,n2=nums[:n],nums[n:]
      new=[]
      for i in range(n):
        new.append(n1[i])
        new.append(n2[i])
      return new
