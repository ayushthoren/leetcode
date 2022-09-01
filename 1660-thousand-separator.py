class Solution(object):
    def thousandSeparator(self, n):
      if len(str(n))<=3: return str(n)
      n=list(str(n))
      i=len(n)%3
      while i<len(n):
        if i!=0:
            n.insert(i, ".")
            i+=4
        else: i+=3
      return "".join(n)
