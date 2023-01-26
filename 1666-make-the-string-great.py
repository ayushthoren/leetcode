class Solution:
    def makeGood(self, s: str) -> str:
        stack=[""]
        for i in s:
            if stack[-1] == i:
                stack.append(i)
            elif stack[-1].lower() == i.lower():
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)
