class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)
        stack,ans=[(0,[0])],[]
        while stack:
            idx,connections=stack.pop()
            if idx==n-1: ans.append(connections); continue
            for i in graph[idx]: stack.append([i,connections+[i]])
        return ans
