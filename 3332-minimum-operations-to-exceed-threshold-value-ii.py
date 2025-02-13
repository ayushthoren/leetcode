class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        n=0
        while nums[0]<k:
            x,y=heapq.heappop(nums),heapq.heappop(nums)
            heapq.heappush(nums,x*2+y)
            n+=1
        return n
