class Solution(object):
    def checkZeroOnes(self, s):
      ones=max([len(o) for o in s.split("0")])
      zeroes=max([len(z) for z in s.split("1")])
      return ones>zeroes
