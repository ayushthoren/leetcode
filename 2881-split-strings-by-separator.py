class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        new=[]
        for i in words:
            tmp=""
            for j in i:
                if j==separator: 
                    if tmp: new.append(tmp); tmp=""
                else: tmp+=j
            if tmp: new.append(tmp)
        return new
