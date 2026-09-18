class Solution:
    def reformatNumber(self, number: str) -> str:
        n, r, i = number.replace(" ", "").replace("-", ""), [], 0
        while len(n)-i > 4: r.append(n[i:i+3]); i += 3
        r.extend([n[i:i+2], n[i+2:]] if len(n)-i == 4 else [n[i:]])
        return "-".join(r)
