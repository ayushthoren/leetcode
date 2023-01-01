class Solution:
    def countPoints(self, rings: str) -> int:
        r={"R":[],"G":[],"B":[]}
        ct=0
        for i in range(len(rings)):
            if rings[i].isnumeric(): r[rings[i-1]].append(int(rings[i]))
        for j in range(10):
            if j in r["R"] and j in r["G"] and j in r["B"]: ct+=1
        return ct
