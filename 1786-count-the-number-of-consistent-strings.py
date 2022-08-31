class Solution(object):
    def countConsistentStrings(self, allowed, words):
      c=0
      for i in words:
        isC=True
        for j in i:
          if j not in allowed: isC=False
        if isC: c+=1
      return c
