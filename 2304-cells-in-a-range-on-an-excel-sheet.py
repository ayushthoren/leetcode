class Solution:
    def cellsInRange(self, s: str) -> List[str]:
      cells=[]
      nRange=sorted([int(s[1]),int(s[4])+1])
      cRange=sorted([ord(s[0]),ord(s[3])+1])
      print(nRange,cRange)
      for i in range(cRange[0],cRange[1]):
        for j in range(nRange[0],nRange[1]):
          cells.append(chr(i)+str(j))
      return cells
