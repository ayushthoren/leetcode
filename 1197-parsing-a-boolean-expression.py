class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack=[]
        for i in expression:
            if i=="(" or i==",": continue
            if i==")":
                t,f=False,False
                while stack[-1] not in ["!","&","|"]:
                    c=stack.pop()
                    if c=="t": t=True
                    if c=="f": f=True
                o=stack.pop()
                if o=="!": stack.append("t" if f else "f")
                elif o=="&": stack.append("t" if t and not f else "f")
                else: stack.append("t" if t or not f else "f")
            else: stack.append(i)
        return stack[-1]=="t"
