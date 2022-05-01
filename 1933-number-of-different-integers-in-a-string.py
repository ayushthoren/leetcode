class Solution:
    def numDifferentIntegers(self, word: str) -> int:
      nums=[]
      if word[0].isdigit(): nums.append("")
      for i in word:
        if i.isdigit():
          nums[-1]+=i
        else: nums.append("")
      return len(set([int(j) for j in nums if j.isdigit()]))
