class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        for i in matrix:
            for j in range(len(i)):
                if i[j]==-1:
                    col=[k[j] for k in matrix]
                    i[j]=max(col)
        return matrix
