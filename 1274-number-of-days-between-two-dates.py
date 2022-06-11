import datetime
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
      date1=[int(d1) for d1 in date1.split("-")]
      date2=[int(d2) for d2 in date2.split("-")]
      dt1=datetime.date(date1[0],date1[1],date1[2])
      dt2=datetime.date(date2[0],date2[1],date2[2])
      diff=dt1-dt2
      return abs(diff.days)
