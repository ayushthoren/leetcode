class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dct,q,tried={},[source],set()
        for e in edges:
            if e[0] not in dct: dct[e[0]]=[]
            if e[1] not in dct: dct[e[1]]=[]
            dct[e[0]].append(e[1])
            dct[e[1]].append(e[0])
        print(dct)
        while q:
            if destination in q: return True
            new=[]
            for i in q:
                for j in dct[i]:
                    if (i,j) not in tried:
                        new.append(j)
                        tried.add((i,j))
            q=list(set(new))
        return False
