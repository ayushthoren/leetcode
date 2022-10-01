class Solution:
    def areNumbersAscending(self, s: str) -> bool:
      nums=[int(i) for i in s.split(" ") if i.isdigit()]
      return nums==sorted(nums) and len(set(nums))==len(nums)
