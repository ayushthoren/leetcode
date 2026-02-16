class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        c, f = Counter(s), defaultdict(list)
        for l, n in c.items(): f[n].append(l)
        print(f)
        m = max(f, key = lambda x: (len(f[x]), x))
        return "".join(f[m])
