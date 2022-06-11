import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
      dayNames=["Monday", "Tuesday", "Wednesday","Thursday", "Friday", "Saturday", "Sunday"]
      return dayNames[datetime.datetime(year,month,day).weekday()]
