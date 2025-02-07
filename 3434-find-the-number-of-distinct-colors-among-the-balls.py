class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        b,c,d={},{},[]
        for i,j in queries:
            if i in b:
                c[b[i]]-=1
                if not c[b[i]]: del c[b[i]]
            b[i],c[j]=j,c.get(j,0)+1
            d.append(len(c))
        return d
