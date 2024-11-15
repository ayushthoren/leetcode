class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=""
        for i in s.lower():
            if i.isalpha() or i.isnumeric(): n+=i
        return n==n[::-1]
