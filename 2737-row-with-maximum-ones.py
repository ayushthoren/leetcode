class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        p=m=0
        for i in range(len(mat)):
            c=mat[i].count(1)
            if c>m: m=c; p=i
        return [p,m]
