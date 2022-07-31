class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
      if name==typed: return True
      if len(typed)<len(name) or name[0]!=typed[0]: return False
      i,j=0,0
      while j<len(typed):
        if i<len(name) and name[i]==typed[j]:
          i+=1
        elif typed[j-1]!=typed[j]: return False
        j+=1
      return i==len(name)
