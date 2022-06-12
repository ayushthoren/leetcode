class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
      yrs=[]
      yrCts={}
      maxPop=0
      minYr=0
      for i in logs:
        for j in range(i[0],i[1]): yrs.append(j)
      for k in set(yrs):
        ct=yrs.count(k)
        yrCts[k]=ct
        if ct>maxPop: maxPop=ct
      for l in yrCts:
        if yrCts[l]==maxPop:
          if minYr==0: minYr=l
          elif minYr>l: minYr=l
      return minYr
