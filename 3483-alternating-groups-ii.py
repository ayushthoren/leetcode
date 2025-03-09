class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors.extend(colors[:k-1])
        ln,l,r=len(colors),0,1
        ans=0
        while r<ln:
            if colors[r]==colors[r-1]:
                l=r; r+=1
                continue
            r+=1
            if r-l<k: continue
            ans+=1; l+=1
        return ans
