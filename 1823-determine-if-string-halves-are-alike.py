class Solution:
    def halvesAreAlike(self, s: str) -> bool:
      vowels=["a","e","i","o","u"]
      s1,s2=s[:len(s)//2],s[(len(s)//2):]
      s1ct,s2ct=0,0
      for i in s1:
        if i.lower() in vowels: s1ct+=1
      for j in s2:
        if j.lower() in vowels: s2ct+=1
      return s1ct==s2ct
