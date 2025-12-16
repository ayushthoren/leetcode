class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r, m = Counter(ransomNote), Counter(magazine)
        for i in r:
            if i not in m or r[i] > m[i]: return False
        return True
