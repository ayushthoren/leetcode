import numpy
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        return numpy.prod([int(i) for i in str(n)])-sum([int(j) for j in str(n)])
