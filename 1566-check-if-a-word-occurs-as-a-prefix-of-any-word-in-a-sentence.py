class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
      s=sentence.split(" ")
      for i in range(len(s)):
        if len(s[i])>=len(searchWord) and s[i][:len(searchWord)]==searchWord: return i+1
      return -1
