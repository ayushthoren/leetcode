class Solution:
    def freqAlphabets(self, s: str) -> str:
      stack=[]
      codes=[]
      new=""
      for i in s:
        stack.append(i)
        if i=="#":
          codes.append(96+int(stack[-3]+stack[-2]))
          for i in range(2): codes.pop(-2)
        else: codes.append(96+int(i))
      for j in codes: new+=chr(j)
      return new
