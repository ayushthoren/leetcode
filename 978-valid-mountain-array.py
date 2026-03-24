class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: return False
        inc, dec = False, False
        for i in range(1, len(arr)):
            if arr[i-1] == arr[i]: return False
            elif arr[i-1] < arr[i]:
                inc = True
                if dec: return False
            else: dec = True
        return dec and inc
