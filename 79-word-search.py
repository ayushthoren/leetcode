class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n,ln=len(board),len(board[0]),len(word)
        def adjacent(e):
            i,j,l,visited=e
            l=word[l]
            out=[]
            if i>0 and board[i-1][j]==l and (i-1,j) not in visited: out.append((i-1,j))
            if i<m-1 and board[i+1][j]==l and (i+1,j) not in visited: out.append((i+1,j))
            if j>0 and board[i][j-1]==l and (i,j-1) not in visited: out.append((i,j-1))
            if j<n-1 and board[i][j+1]==l and (i,j+1) not in visited: out.append((i,j+1))
            return out

        def dfs(i,j):
            stack=[[i,j,1,set([(i,j)])]]
            while stack and stack[-1][2]<ln:
                p=stack.pop()
                adj=adjacent(p)
                for y,x in adj:
                    stack.append([y,x,p[2]+1,set([(y,x)])|p[3]])
            return stack


        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if dfs(i,j): return True
        return False
