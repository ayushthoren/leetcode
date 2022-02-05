class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
      new=s
      for i in range(len(s)):
        new=new[:indices[i]]+s[i]+new[indices[i]+1:]
      return new
