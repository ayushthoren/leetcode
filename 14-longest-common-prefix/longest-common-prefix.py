class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre,strs="",sorted(strs,key=len)
        for i in range(len(strs[0])):
            for j in strs:
                if j[i]!=strs[0][i]: return pre
            pre+=strs[0][i]
        return pre