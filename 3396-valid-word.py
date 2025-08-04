class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3: return False
        v, c = False, False
        for i in word:
            if i.isalpha():
                if i.lower() in "aeiou": v = True
                else: c = True
            elif not i.isdigit(): return False
        return v and c
