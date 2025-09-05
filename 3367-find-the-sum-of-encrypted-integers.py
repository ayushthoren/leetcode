class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        return sum(int(max(i) * len(i)) for i in map(str, nums))
