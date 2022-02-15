class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
      s1, s2 = s1.split(" "), s2.split(" ")
      uncommon = []
      for i in s1:
        if s1.count(i)<2 and i not in s2: uncommon.append(i)
      for i in s2:
        if s2.count(i)<2 and i not in s1: uncommon.append(i)
      return uncommon
