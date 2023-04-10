class Solution:
    def minMaxDifference(self, num: int) -> int:
        p=set()
        for i in str(num):
            for j in range(10):
                p.add(int(str(num).replace(i,str(j))))
        return max(p)-min(p)
