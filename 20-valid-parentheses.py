class Solution:
    def isValid(self, s: str) -> bool:
        stack=[" "]
        for i in s:
            if i==")":
                if stack[-1]=="(": stack.pop(-1)
                else: return False
            elif i=="]":
                if stack[-1]=="[": stack.pop(-1)
                else: return False
            elif i=="}":
                if stack[-1]=="{": stack.pop(-1)
                else: return False
            else: stack.append(i)
        if stack==[" "]: return True
        return False
