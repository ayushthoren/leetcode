class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sums=[]
        for i in range(0,len(arr)+1):
            for j in range(i,len(arr)+1):
                if (j-i)%2==1:
                    sums.append(arr[i:j])
        return sum([sum(k) for k in sums])
