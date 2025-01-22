class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        o="".join(sorted(map(str,nums),key=lambda x: x*10,reverse=True))
        return o if o[0]!="0" else "0"
