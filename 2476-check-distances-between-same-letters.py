class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        ids={}
        for i in s:
            if i not in ids: ids[i]=[False,-1]
        for j in range(len(s)):
            if ids[s[j]][0]==False: ids[s[j]]=[True,j]
            else:
                if (j-ids[s[j]][1])-1!=distance[ord(s[j])-97]: return False
        return True
