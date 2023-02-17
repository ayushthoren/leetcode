class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ct=0
        for i in text.split(" "):
            good=True
            for j in brokenLetters:
                if j in i: good=False
            if good: ct+=1
        return ct
