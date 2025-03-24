class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        l,t=0,0
        meetings.sort()
        for s,e in meetings:
            if s>l+1: t+=s-l-1
            l=max(l,e)
        return t+days-l
