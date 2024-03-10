class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxx=""
        for i in range(len(num)-2):
            if num[i]==num[i+1] and num[i]==num[i+2]:
                tmp=num[i]+num[i+1]+num[i+2]
                if not maxx or int(tmp)>=int(maxx): maxx=tmp
        return maxx
