class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        d = 0
        for x in range(len(strs[0])):
            for y in range(1, len(strs)):
                if strs[y][x] < strs[y-1][x]:
                    d +=1; break
        return d
