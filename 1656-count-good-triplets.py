class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ln,ct=len(arr),0
        for i in range(ln):
            for j in range(i+1,ln):
                for k in range(j+1,ln):
                    if abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c:
                        ct+=1
        return ct
