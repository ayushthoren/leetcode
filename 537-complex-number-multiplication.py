class Solution(object):
    def complexNumberMultiply(self, num1, num2):
      num1,num2=num1.split("+"),num2.split("+")
      a,b,c,d=int(num1[0]),int(num1[1][:-1]),int(num2[0]),int(num2[1][:-1])
      f,o,i,l=0,0,0,0
      f=a*c
      o=a*d
      i=b*c
      l=(b*d)*-1
      real,img=f+l,o+i
      return str(real)+"+"+str(img)+"i"
