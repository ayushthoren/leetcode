class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        prev=None
        after=[]
        for i in nums:
            if prev==key: after.append(i)
            prev=i
        return max(set(after), key = after.count)
