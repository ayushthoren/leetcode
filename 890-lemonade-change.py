class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
      change=[]
      for i in bills:
        if i==5: change.append(5)
        if i==10:
          if 5 in change: change.remove(5)
          else: return False
          change.append(10)
        if i==20:
          if 5 in change and 10 in change:
            change.remove(5)
            change.remove(10)
          elif change.count(5)>2:
            for i in range(3): change.remove(5)
          else: return False
      return True
