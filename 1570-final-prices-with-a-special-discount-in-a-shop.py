class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
      new=[]
      for i in range(len(prices)):
        less=False
        for j in prices[i+1::]:
          if j<=prices[i]: less=j; break
        if less: new.append(prices[i]-less)
        else: new.append(prices[i])
      return new
