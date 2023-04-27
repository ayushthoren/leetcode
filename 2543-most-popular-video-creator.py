class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        popularity={}
        most={}
        for creator,id,view in zip(creators,ids,views):
            if creator not in popularity: popularity[creator]=view
            else: popularity[creator]+=view
            if creator not in most: most[creator]=(view,id)
            else:
                if view>most[creator][0]: most[creator]=(view,id)
                if view==most[creator][0] and id<most[creator][1]: most[creator]=(view,id)  
        maxp=max(popularity.values())
        mostp=[]
        for i in popularity:
            if popularity[i]==maxp: mostp.append([i,most[i][1]])
        return mostp
