class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ct = 0
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == "X":
                    if (y == 0 or board[y-1][x] == ".") and (x == 0 or board[y][x-1] == "."): ct+=1
        return ct
