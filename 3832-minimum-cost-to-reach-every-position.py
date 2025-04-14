class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        m,mins=cost[0],[cost[0]]
        for i in range(1,len(cost)):
            m=min(m,cost[i])
            mins.append(m)
        return mins
