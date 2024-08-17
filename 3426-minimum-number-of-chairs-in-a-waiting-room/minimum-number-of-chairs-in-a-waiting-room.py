class Solution:
    def minimumChairs(self, s: str) -> int:
        taken,available=0,0
        for i in s:
            if i=="E":
                taken+=1
                if available>0: available-=1
            if i=="L": taken-=1; available+=1
        return taken+available