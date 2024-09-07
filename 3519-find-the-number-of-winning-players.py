class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        picks,winners={},0
        for i in pick:
            if i[0] not in picks: picks[i[0]]=[]
            picks[i[0]].append(i[1])
        print(picks)
        for j in picks:
            maxct=picks[j].count(max(set(picks[j]),key=picks[j].count))
            if maxct>j: winners+=1
        return winners
