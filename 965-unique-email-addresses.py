class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        u = set()
        for e in emails:
            l, d = e.split("@")
            l = l.split("+")[0].replace(".", "")
            u.add(f"{l}@{d}")
        return len(u)
