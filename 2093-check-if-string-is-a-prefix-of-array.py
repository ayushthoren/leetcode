class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        p=""
        for i in words:
            p+=i
            if p==s: return True
        return False
