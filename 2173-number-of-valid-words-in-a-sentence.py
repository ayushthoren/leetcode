class Solution:
  def __init__(self):
    self.punctuation=["!",".",","]
  def __checkHyphen(self, word: str) -> bool:
    if word.count("-")>1: return False
    if word.count("-")==1:
      i=word.index("-")
      if i==0 or i==len(word)-1: return False
      if word[i-1] in self.punctuation or word[i+1] in self.punctuation: return False
    return True
  def __checkPunctuation(self, word: str) -> bool:
    for i in word:
      if not i.isalpha() and i!="-":
        idx=word.index(i)
        if i not in self.punctuation: return False
        if idx<len(word)-1: return False
    return True    
  def countValidWords(self, sentence: str) -> bool:
    sentence=sentence.split(" ")
    valid=0
    for i in sentence:
      if i!="" and self.__checkHyphen(i) and self.__checkPunctuation(i): valid+=1
    return valid
