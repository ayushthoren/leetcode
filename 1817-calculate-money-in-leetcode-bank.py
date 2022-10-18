class Solution:
    def totalMoney(self, n: int) -> int:
      days,sub=0,-1
      money=0
      for i in range(n):
        money+=i-sub
        days+=1
        if days==7: days=0; sub+=6
      return money
