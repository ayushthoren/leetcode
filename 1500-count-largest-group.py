class Solution:
    def countLargestGroup(self, n: int) -> int:
      groups={s:[] for s in range(1,n+1)}
      maxLen=0
      for i in range(1,n+1):
        summ=sum([int(j) for j in str(i)])
        if summ<=n:
          groups[summ].append(i)
          if len(groups[summ])>maxLen: maxLen=len(groups[summ])
      return len([j for j in groups if len(groups[j])==maxLen])
