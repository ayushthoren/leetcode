class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ge=set(sum(grid,[]))
        if ge=={1}: return -1
        if ge=={0}: return 0

        def checkAdjacent(x,y):
            out=[]
            if 0<=x-1 and grid[y][x-1]==1: out.append([x-1,y])
            if n>x+1 and grid[y][x+1]==1: out.append([x+1,y])
            if 0<=y-1 and grid[y-1][x]==1: out.append([x,y-1])
            if m>y+1 and grid[y+1][x]==1: out.append([x,y+1])
            return out

        q,m,n,ct=[],len(grid),len(grid[0]),-1
        for y in range(m):
            for x in range(n):
                if grid[y][x]==2: q.append([x,y])
        while q:
            ct+=1
            new,newq=grid,[]
            for i in q:
                adjFresh=checkAdjacent(i[0],i[1])
                for j in adjFresh:
                    newq.append(j)
                    new[j[1]][j[0]]=2
            grid,q=new,newq
        for g in grid:
            if 1 in g: return -1
        return ct
