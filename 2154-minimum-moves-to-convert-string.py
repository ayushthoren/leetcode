class Solution:
    def minimumMoves(self, s: str) -> int:
        ct,s=0,list(s)
        for i in range(len(s)-2):
            if s[i]=="X":
                ct+=1
                s[i]=s[i+1]=s[i+2]="O"
        return ct+1 if s[-1]=="X" or s[-2]=="X" else ct
