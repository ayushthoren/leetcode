class Solution:
    def getLucky(self, s: str, k: int) -> int:
      s="".join([str(int(ord(i))-96) for i in s])
      summ=sum([int(j) for j in s])
      for i in range(k-1):
        summ=sum(int(k) for k in str(summ))
      return summ
