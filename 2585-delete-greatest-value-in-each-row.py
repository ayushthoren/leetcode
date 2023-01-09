class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        summ=0
        while grid[0]:
            maxes=[]
            for i in grid:
                maxes.append(max(i))
                i.remove(max(i))
            summ+=max(maxes)
        return summ
