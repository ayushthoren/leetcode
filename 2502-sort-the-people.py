class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        info={heights[i]:names[i] for i in range(len(names))}
        return [info[j] for j in sorted(info.keys())[::-1]]
