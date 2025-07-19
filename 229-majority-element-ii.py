class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [e for e, c in Counter(nums).items() if c > len(nums) // 3]
