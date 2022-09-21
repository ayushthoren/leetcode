class Solution:
    def greatestLetter(self, s: str) -> str:
      ltr=0
      for i in s:
        if i.upper() in s and i.lower() in s and ord(i.upper())>ltr: ltr=ord(i.upper())
      if ltr==0: return ""
      return chr(ltr)
