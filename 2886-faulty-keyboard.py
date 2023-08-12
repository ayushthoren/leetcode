class Solution:
    def finalString(self, s: str) -> str:
        new=""
        for i in s:
            if i=="i": new=new[::-1]
            else: new+=i
        return new
