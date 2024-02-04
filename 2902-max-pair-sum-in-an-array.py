class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nm=[max(map(int, list(str(n)))) for n in nums]
        sums=[]
        for i in range(len(nm)):
            for j in range(len(nm)):
                if nm[i]==nm[j] and i!=j: sums.append(nums[i]+nums[j])
        return max(sums) if sums else -1
