class Solution:
    def romanToInt(self, s: str) -> int:
      map,total={"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000},0
      for i in range(len(s)-1):
        if map[s[i]]>=map[s[i+1]]: total+=map[s[i]]
        else: total-=map[s[i]]
      return total+map[s[-1]]
