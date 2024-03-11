class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        valid=[p for p in points if p[0]==x or p[1]==y][::-1]
        nearest={"idx":-1,"dist":None}
        for i in range(len(valid)):
            d=abs(x-valid[i][0])+abs(y-valid[i][1])
            if nearest["dist"]==None or nearest["dist"]>=d:
                nearest["dist"]=d
                nearest["idx"]=points.index(valid[i])
        return nearest["idx"]
