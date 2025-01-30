class Solution:
    def checkIfPangram(self,sentence: str) -> bool:
        a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in sentence: a[ord(i)-97]=True
        for l in a:
            if l!=True: return False
        return True
