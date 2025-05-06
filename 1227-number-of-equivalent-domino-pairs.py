class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        cts,r=defaultdict(lambda: defaultdict(int)),0
        for i in dominoes:
            a,b=(i[0],i[1]) if i[0]>i[1] else (i[1],i[0])
            if cts[a][b]: r+=cts[a][b]
            cts[a][b]+=1
        return r
