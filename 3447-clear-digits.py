class Solution:
    def clearDigits(self, s: str) -> str:
        s,i,l=list(s),0,len(s)
        while i<l:
            if s[i].isnumeric():
                s.pop(i); l-=1
                for j in reversed(range(i)):
                    if s[j].isalpha(): s.pop(j); l-=1; break
                i-=1
            else: i+=1
        return "".join(s)
