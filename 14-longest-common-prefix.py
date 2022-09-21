class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      strs.sort(key=len)
      prefix=strs[0]
      for i in strs:
        for j in range(len(i)):
          if len(prefix)-1>=j and i[j]!=prefix[j]: prefix=prefix[:j]
      return prefix
