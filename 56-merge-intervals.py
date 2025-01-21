class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        good,ln=False,len(intervals)
        while not good:
            good=True
            for i in range(ln-1):
                if intervals[i][1]>=intervals[i+1][0]:
                    if intervals[i+1][1]>intervals[i][1]:
                        intervals[i][1]=intervals[i+1][1]
                    intervals.pop(i+1); ln-=1
                    good=False
                    break
        return intervals
