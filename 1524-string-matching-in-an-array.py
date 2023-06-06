class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        subs=[]
        for i in words:
            for j in words:
                if i in j and i not in subs and j!=i:
                    subs.append(i)
        return subs
