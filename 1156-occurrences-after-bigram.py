class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
      splitted=text.split(" ")
      after=[]
      for i in range(len(splitted)-2):
        if splitted[i]==first:
          if splitted[i+1]==second:
            after.append(splitted[i+2])
      return after
