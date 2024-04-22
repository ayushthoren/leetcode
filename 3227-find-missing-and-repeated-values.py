class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        grid=sum(grid,[])
        missing=list(set(range(1,len(grid)+1)).difference(set(grid)))[0]
        repeated=max(grid,key=grid.count)
        return [repeated,missing]
