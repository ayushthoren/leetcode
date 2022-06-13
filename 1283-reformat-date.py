class Solution:
    def reformatDate(self, date: str) -> str:
      months=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
      date=date.split(" ")
      new=date[2]+"-"
      if len(str(months.index(date[1])+1))<2: new+="0"
      new+=str(months.index(date[1])+1)+"-"
      if len(date[0])<4: new+="0"
      new+=date[0][0:-2]
      return new
