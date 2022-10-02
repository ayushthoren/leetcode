class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
      if len(arr)==1: return [-1]
      new=[]
      for i in range(len(arr)-1):
        new.append(max(arr[i+1:]))
      new.append(-1)
      return new
