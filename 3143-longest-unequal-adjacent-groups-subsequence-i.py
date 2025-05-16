class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        o,l=[],0 if groups[0]==1 else 1
        for i in range(1,len(words)):
            if groups[i]!=groups[i-1]: o.append(words[i-1]); l=groups[i-1]
        if groups[-1]!=l: o.append(words[-1])
        return o
