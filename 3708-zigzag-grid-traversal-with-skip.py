class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        z=[]
        for i in range(len(grid)): z+=grid[i] if i%2==0 else grid[i][::-1]
        return [z[j] for j in range(0,len(z),2)]
