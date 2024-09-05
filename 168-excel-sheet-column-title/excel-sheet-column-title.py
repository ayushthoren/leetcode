class Solution(object):
    def convertToTitle(self, columnNumber):
      title=""
      while columnNumber>0:
        columnNumber-=1
        mod=columnNumber%26
        title+=chr(mod+65)
        columnNumber//=26
      return title[::-1]