class Solution:
    def sortVowels(self, s: str) -> str:
        s,ls,v,l=list(s),len(s),["A","E","I","O","U","a","e","i","o","u"],[]
        for i in range(ls):
            if s[i] in v:
                l.append(s[i])
                s[i]=None
        l.sort(key=lambda x: ord(x))
        for j in range(ls):
            if not s[j]: s[j]=l.pop(0)
        return "".join(s)
