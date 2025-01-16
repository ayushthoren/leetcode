class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def getVal(s):
            o=""
            for i in s: o+=str(ord(i)-97)
            return int(o)
        return getVal(firstWord)+getVal(secondWord)==getVal(targetWord)
