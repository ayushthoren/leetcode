class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        w,c,ans=defaultdict(int),defaultdict(list),[]
        for i in words: w[i]+=1
        for j in w: c[w[j]].append(j)
        c=sorted(c.items(), reverse=True)
        for l in c: ans.extend(sorted(l[1]))
        return ans[:k]
