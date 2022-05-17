class Solution:
    def reorderSpaces(self, text: str) -> str:
      spaceCt=text.count(" ")
      text=text.split(" ")
      newText=text.copy()
      s=""
      for i in text:
        if i=="": newText.remove(i)
      if len(newText)==1: return newText[0]+(" "*spaceCt)
      for j in range(len(newText)-1):
        s+=newText[j]+(" "*((spaceCt-(spaceCt%(len(newText)-1)))//(len(newText)-1)))
      return s+newText[-1]+(" "*(spaceCt%(len(newText)-1)))
