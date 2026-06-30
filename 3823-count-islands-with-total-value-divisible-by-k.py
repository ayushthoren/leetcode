class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        def island(y, x):
            s = 0
            q = deque()

            def zero(y, x):
                s = grid[y][x]
                grid[y][x] = 0
                q.append((y,x))
                return s

            s += zero(y, x)

            while q:
                i = q.popleft()
                if i[0] - 1 >= 0 and grid[i[0]-1][i[1]] != 0: s += zero(i[0]-1, i[1])
                if i[0] + 1 < len(grid) and grid[i[0]+1][i[1]] != 0: s += zero(i[0]+1, i[1])
                if i[1] - 1 >= 0 and grid[i[0]][i[1]-1] != 0: s += zero(i[0], i[1]-1)
                if i[1] + 1 < len(grid[i[0]]) and grid[i[0]][i[1]+1] != 0: s += zero(i[0], i[1]+1)

            return s

        return sum(grid[y][x] != 0 and island(y, x) % k == 0 for y in range(len(grid)) for x in range(len(grid[y])))
