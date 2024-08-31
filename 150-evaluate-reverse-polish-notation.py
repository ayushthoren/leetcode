class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
      operators=["+","-","*","/"]
      stack=[]
      for i in tokens:
        if i in operators:
          if i=="/": new=str(int(eval(stack[-2]+i+stack[-1])))
          else: new=str(eval(stack[-2]+i+stack[-1]))
          stack=stack[:-2]
          stack.append(new)
        else: stack.append(i)
      return int(stack[0])
