class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        m = {order[c]: c for c in range(len(order))}
        w = [[m[j] for j in i] for i in words]
        for i in range(len(w)-1):
            if w[i] > w[i+1]: return False
        return True
