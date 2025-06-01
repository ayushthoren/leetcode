class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        l,u=[False]*26,[False]*26
        for c in word:
            if "a"<=c<="z": l[ord(c)-97]=True
            else: u[ord(c)-65]=True
        return sum(l[i] and u[i] for i in range(26))
