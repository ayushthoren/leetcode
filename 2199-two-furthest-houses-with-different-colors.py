class Solution(object):
    def maxDistance(self, colors):
        p=[]
        for i in range(len(colors)):
            for j in reversed(range(i,len(colors))):
                if colors[i]!=colors[j]: p.append(j-i)
        return max(p)
