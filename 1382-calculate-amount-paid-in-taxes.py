class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
      tax=0
      paid=0
      for i in brackets:
        i[0]-=paid
        if income>=i[0]:
          tax+=i[0]*(i[1]/100)
          income-=i[0]
        elif income<i[0]:
          tax+=income*(i[1]/100)
          income=0
        paid+=i[0]
      return tax
