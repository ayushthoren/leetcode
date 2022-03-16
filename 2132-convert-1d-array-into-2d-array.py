class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
      if m*n!=len(original): return []
      arr=[]
      for i in range(1,m+1):
        arr.append(original[n*(i-1):n*i])
      return arr
