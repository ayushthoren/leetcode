class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
      maxUnits=0

      from functools import cmp_to_key
      def compare(i1,i2):
        return i2[1]-i1[1]
      boxTypes.sort(key=cmp_to_key(compare))

      for j in boxTypes:
        if truckSize>=j[0]:
          truckSize-=j[0]
          maxUnits+=j[1]*j[0]
        else:
          maxUnits+=j[1]*truckSize
          return maxUnits
      return maxUnits
