class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        m=[]
        for i in range(len(mat)):
            ct=mat[i].count(1)
            if not m or ct>m[1]: m=[i,ct]
        return m
