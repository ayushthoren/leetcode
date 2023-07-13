class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        new=[[0 for cn in range(c)] for rn in range(r)]
        omat=mat
        mat=[x for y in mat for x in y]
        if len(mat)!=r*c: return omat
        pt=0
        for i in range(len(new)):
            for j in range(len(new[i])):
                new[i][j]=mat[pt]
                pt+=1
        return new
