class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ct = 0
        for i in range(low, high+1):
            i = str(i)
            li = len(i)
            if li % 2 == 0 and sum(list(map(int,[*i[:li//2]]))) == sum(list(map(int,[*i[li//2:]]))): ct+=1
        return ct