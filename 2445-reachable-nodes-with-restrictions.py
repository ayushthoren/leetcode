class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        a, restricted = defaultdict(list), set(restricted)
        for x, y in edges: a[x].append(y); a[y].append(x)
        
        v, q = {0}, [0]
        while q:
            i = q.pop()
            for e in a[i]:
                if e not in v and e not in restricted:
                    v.add(e); q.append(e)

        return len(v)
