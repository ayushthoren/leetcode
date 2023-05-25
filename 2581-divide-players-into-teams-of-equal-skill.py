class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill,teams=sorted(skill),[]
        for i in range(len(skill)//2): teams.append([skill[i],skill[-(i+1)]])
        for j in teams:
            if sum(j)!=sum(teams[0]): return -1
        return sum(k[0]*k[1] for k in teams)
