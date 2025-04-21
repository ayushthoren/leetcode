class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        c,mi,ma=0,0,0
        for d in differences:
            c+=d
            mi=min(mi,c)
            ma=max(ma,c)
        n=(upper-ma)-(lower-mi)+1
        return max(0,n)
