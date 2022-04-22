class Solution:
    def makeFancyString(self, s: str) -> str:
      stack=""
      for i in s:
        if len(stack)>=2:
          if stack[-1]!=i or stack[-2]!=stack[-1]: stack+=i
        else: stack+=i
      return stack
