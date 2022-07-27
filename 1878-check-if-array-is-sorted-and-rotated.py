class Solution:
    def check(self, nums: List[int]) -> bool:
      srt=sorted(nums)
      for i in nums:
        srt.append(srt[0])
        srt=srt[1:]
        if srt==nums: return True
      return False
