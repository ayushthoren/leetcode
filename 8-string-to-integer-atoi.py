class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        if not s: return 0
        sgn,ls,i,r=1,len(s),0,0
        if s[0]=="+": i+=1
        elif s[0]=="-": sgn=-1; i+=1
        while i<ls and s[i].isdigit():
            r=r*10+int(s[i])
            i+=1
        r*=sgn
        if r>2147483647: return 2147483647
        if r<-2147483648: return -2147483648
        return r
