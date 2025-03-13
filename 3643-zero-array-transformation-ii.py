class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        ln,lq,s,ct=len(nums),len(queries),0,0
        diff=[0]*(ln+1)
        for i in range(ln):
            while s+diff[i]<nums[i]:
                ct+=1
                if ct>lq: return -1
                l,r,v=queries[ct-1]
                if r>=i:
                    diff[max(l,i)]+=v
                    diff[r+1]-=v
            s+=diff[i]
        return ct
