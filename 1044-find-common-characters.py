class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
      cts={chr(i):100 for i in range(97,123)}
      for i in words:
        tmpCts={}
        for j in i:
          if j not in tmpCts: tmpCts[j]=0
          tmpCts[j]+=1
        for k in tmpCts:
          if k not in cts: cts[k]=tmpCts[k]
          else:
            if cts[k]>tmpCts[k]: cts[k]=tmpCts[k]
        for l in cts:
          if l not in tmpCts: cts[l]=0
      new=[]
      for m in cts:
        for n in range(cts[m]): new.append(m)
      return new
