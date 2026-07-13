class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        q, p = set([0]), 1
        while any(isConnected):
            if len(q) == 0:
                p += 1
                for x in range(len(isConnected)):
                    if isConnected[x]: q = set([x]); break

            t = set()
            for i in q:
                if isConnected[i]:
                    n = isConnected[i]
                    for j in range(len(n)):
                        if n[j]: t.add(j)
                    isConnected[i] = 0
            q = t
        return p
