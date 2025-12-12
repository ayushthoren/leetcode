class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper(); l = len(s)
        f = l % k or k; n = [s[:f]]
        for i in range(f, l, k): n.append(s[i:i+k])
        return "-".join(n)
