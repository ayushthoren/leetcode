class Solution(object):
    def minTimeToType(self, word):
      l="a"
      t=0
      def minTime(l1,l2):
        sm, lg = min(l1,l2), max(l1,l2)
        cc = ord(lg)-ord(sm)
        cl = (ord("z")+1-ord(lg))+(ord(sm)-ord("a"))
        return min(cc,cl)
      for i in word:
        t+=minTime(i,l)+1
        l=i
      return t
