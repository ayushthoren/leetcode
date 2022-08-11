class Solution(object):
    def sortEvenOdd(self, nums):
      numsl=len(nums)
      even=sorted([nums[e] for e in range(numsl) if e%2==0])
      odd=sorted([nums[o] for o in range(numsl) if o%2==1])
      ei,oi=0,len(odd)-1
      le,lo=len(even),len(odd)
      new=[0 for l in range(numsl)]
      for i in range(numsl):
        if i%2==0: new[i]=even[ei]; ei+=1
        else: new[i]=odd[oi]; oi-=1
      return new
