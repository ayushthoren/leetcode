class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        dists={}
        for y in range(rows):
            for x in range(cols):
                dist=abs(y-rCenter)+abs(x-cCenter)
                if dist not in dists: dists[dist]=[]
                dists[dist].append([y,x])
        keys=sorted(list(dists.keys()))
        sDists={i:dists[i] for i in keys}
        r=[]
        for j in sDists:
            for k in sDists[j]: r.append(k)
        return r
