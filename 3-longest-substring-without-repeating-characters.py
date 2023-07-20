class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        u=set()
        l=0
        largest=0
        for i in range(len(s)):
            while s[i] in u:
                u.remove(s[l])
                l+=1
            u.add(s[i])
            if largest<(i-l)+1: largest=(i-l)+1
        return largest
