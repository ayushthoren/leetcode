class Solution(object):
    def mostCommonWord(self, paragraph, banned):
      paragraph=paragraph.lower()
      punctuation=[" ",".",",","!","?",";",":","\'"]
      para=[""]
      for i in paragraph:
        if i in punctuation: 
          if para[-1]!="": para.append("")
        else: para[-1]=para[-1]+i
      cts={}
      for j in para:
        if j not in banned and j!="":
          if j not in cts: cts[j]=0
          cts[j]+=1
      return max(cts,key=cts.get)
