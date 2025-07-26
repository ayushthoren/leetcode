class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            s, e, g = 0, len(i) - 1, True
            while s < e:
                if i[s] != i[e]: g = False; break
                s += 1; e -= 1
            if g: return i
        return ""
