class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num1,num2,num3=str(num1).zfill(4),str(num2).zfill(4),str(num3).zfill(4)
        return int(min(num1[0],num2[0],num3[0])+min(num1[1],num2[1],num3[1])+min(num1[2],num2[2],num3[2])+min(num1[3],num2[3],num3[3]))
