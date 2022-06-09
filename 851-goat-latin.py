class Solution:
    def toGoatLatin(self, sentence: str) -> str:
      vowels=["a","e","i","o","u"]
      sentence=sentence.split(" ")
      new=[]
      for i in range(len(sentence)):
        if sentence[i][0].lower() in vowels:
          new.append(sentence[i]+"ma"+("a"*(i+1)))
        else:
          new.append(sentence[i][1:]+sentence[i][0]+"ma"+("a"*(i+1)))
      return " ".join(new)
