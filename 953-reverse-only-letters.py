class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        r,p=[],-1
        for i in range(len(s)):
            if s[i].isalpha():
                while not s[p].isalpha(): p-=1
                r.append(s[p])
                p-=1
            else: r.append(s[i])
        return "".join(r)
