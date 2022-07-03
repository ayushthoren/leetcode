class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
      if ch not in word: return word
      pre=""
      hasPre=False
      for i in word:
        if not hasPre:
          if i==ch: pre+=i; pre=pre[::-1]; hasPre=True
          else: pre+=i
        else: pre+=i
      return pre
