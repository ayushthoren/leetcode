class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apple=sum(apple)
        capacity=sorted(capacity)[::-1]
        s=0
        for i in range(len(capacity)):
            s+=capacity[i]
            if s>=apple: return i+1
