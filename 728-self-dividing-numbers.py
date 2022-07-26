class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
      selfDiv=[]
      isSelfDiv=True
      for i in range(left,right+1):
        isSelfDiv=True
        for j in str(i):
          if j=="0" or i%int(j)!=0: isSelfDiv=False
        if isSelfDiv: selfDiv.append(i)
      return selfDiv
