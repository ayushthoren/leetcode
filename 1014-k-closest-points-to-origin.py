class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return [p for p, d in sorted(zip(points, [((i[0]**2)+(i[1]**2))**0.5 for i in points]),key=lambda x: x[1])][:k]
