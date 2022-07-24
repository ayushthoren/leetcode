class Solution:
    def tribonacci(self, n: int) -> int:
      if n==0: return 0
      if n<3: return 1
      arr=[0 for i in range(n)]
      arr[0],arr[1]=0,1
      summ=1
      for j in range(n-2):
        arr[j+2]=summ
        summ+=arr[j+1]+arr[j]
        print(arr)
      return arr[-1]+arr[-2]+arr[-3]
