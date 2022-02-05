class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
      occurences=[]
      for i in set(arr):
        if arr.count(i) in occurences: return False
        occurences.append(arr.count(i))
      return True
