class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        m=0
        for i in range(len(number)):
            if number[i]==digit:
                wo=number[:i]+number[i+1:]
                if int(wo)>m: m=int(wo)
        return str(m)
