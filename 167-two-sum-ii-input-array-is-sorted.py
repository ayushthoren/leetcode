class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
      p1, p2 = 0, -1
      while numbers[p1]+numbers[p2]!=target:
        summ=numbers[p1]+numbers[p2]
        if summ<target: p1+=1
        if summ>target: p2-=1
      return [p1+1,len(numbers)-abs(p2+1)]
