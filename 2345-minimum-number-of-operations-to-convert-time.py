class Solution(object):
    def convertTime(self, current, correct):
      current,correct=current.split(":"),correct.split(":")
      cur,cor=(int(current[0])*60)+int(current[1]),(int(correct[0]))*60+int(correct[1])
      toAdd=cor-cur
      ops=0
      while toAdd:
        if toAdd>=60: toAdd-=60; ops+=1
        elif toAdd>=15: toAdd-=15; ops+=1
        elif toAdd>=5: toAdd-=5; ops+=1
        elif toAdd>=1: toAdd-=1; ops+=1
      return ops
