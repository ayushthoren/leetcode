class Solution:
    def constructRectangle(self, area: int) -> List[int]:
      pairs=[]
      maybe=[]
      for i in range(1,area+1):
        if area%i==0 and i>=area//i: pairs.append([i,area//i])
      for j in pairs:
        dist=abs(j[0]-j[1])
        if maybe==[] or dist<maybe[0]: maybe=[dist, j]
      return maybe[1]
