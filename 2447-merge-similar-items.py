class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        ret={}
        for i in items1:
            if i[0] not in ret: ret[i[0]]=0
            ret[i[0]]+=i[1]
        for j in items2:
            if j[0] not in ret: ret[j[0]]=0
            ret[j[0]]+=j[1]
        keys=sorted(list(ret.keys()))
        sret={l:ret[l] for l in keys}
        return [[k,sret[k]] for k in sret]
