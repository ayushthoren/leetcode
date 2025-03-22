class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        ln,ans=len(s),""
        for i in range(ln): ans+=s[(i+k)%ln]
        return ans
