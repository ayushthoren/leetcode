class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        colors,ct=[colors[-1]]+colors+[colors[0]],0
        for i in range(1,len(colors)-1):
            if colors[i-1]==colors[i+1] and colors[i-1]!=colors[i]: ct+=1
        return ct
