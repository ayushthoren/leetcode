class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        w1,w2=[0]*26,[0]*26
        for i in word1: w1[ord(i)-97]+=1
        for j in word2: w2[ord(j)-97]+=1
        for k in range(26):
            if abs(w1[k]-w2[k])>3: return False
        return True
