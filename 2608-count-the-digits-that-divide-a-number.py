class Solution:
    def countDigits(self, num: int) -> int:
        ct=0
        for i in str(num):
            if num%int(i)==0: ct+=1
        return ct
