class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        mb,mt=events[0]
        for i in range(1,len(events)):
            d=events[i][1]-events[i-1][1]
            if d>mt: mb,mt=events[i][0],d
            if d==mt: mb=min(mb,events[i][0])
        return mb
