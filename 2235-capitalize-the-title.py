class Solution:
    def capitalizeTitle(self, title: str) -> str:
      new=[]
      for i in title.lower().split(" "):
        if len(i)>2: new.append(i[0].upper()+i[1:])
        else: new.append(i)
      return " ".join(new)
