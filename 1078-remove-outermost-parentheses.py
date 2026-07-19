class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        r, c = [], 0
        for i in s:
            if i == "(":
                if c > 0: r.append(i)
                c += 1
            else:
                if c > 1: r.append(i)
                c -= 1
        return "".join(r)
