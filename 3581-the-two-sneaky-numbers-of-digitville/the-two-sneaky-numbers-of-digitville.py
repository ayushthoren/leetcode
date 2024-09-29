class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        cts,out={},[]
        for i in nums:
            if i not in cts: cts[i]=0
            cts[i]+=1
            if cts[i]==2: out.append(i)
        return out