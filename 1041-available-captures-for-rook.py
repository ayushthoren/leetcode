class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
      ct=0
      isBishop=False
      for i in range(len(board)):
        for j in range(len(board[i])):
          if board[i][j]=="R":
            #North
            isBishop=False
            for n in board[:i][::-1]:
              if n[j]=="B": isBishop=True
              if n[j]=="p" and not isBishop: ct+=1; break

            #East
            isBishop=False
            for e in board[i][j:]:
              if e=="B": isBishop=True
              if e=="p" and not isBishop: ct+=1; break

            #South
            isBishop=False
            for s in board[i:]:
              if s[j]=="B": isBishop=True
              if s[j]=="p" and not isBishop: ct+=1; break

            #West
            isBishop=False
            for w in board[i][:j][::-1]:
              if w=="B": isBishop=True
              if w=="p" and not isBishop: ct+=1; break
      return ct
