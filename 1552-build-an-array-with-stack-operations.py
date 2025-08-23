class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        s, i = [], 0
        for n in target:
            while i < n - 1:
                s.append("Push"); s.append("Pop")
                i += 1
            s.append("Push")
            i += 1
        return s
