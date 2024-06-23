class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub=[]
        removed=0
        longest=0
        for i in range(len(s)):
            while s[i] in sub: sub.pop(0); removed+=1
            sub.append(s[i])
            ln=(i+1)-removed
            if ln>longest: longest=ln
        return longest
