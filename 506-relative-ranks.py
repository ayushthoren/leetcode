class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorts=sorted(score)[::-1]
        print(sorts)
        ranks=[]
        for i in score:
            r=sorts.index(i)
            if r==0: ranks.append("Gold Medal")
            elif r==1: ranks.append("Silver Medal")
            elif r==2: ranks.append("Bronze Medal")
            else: ranks.append(str(r+1))
        return ranks
