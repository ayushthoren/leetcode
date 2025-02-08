class NumberContainers:

    def __init__(self):
        self.c,self.n={},defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.c[index]=number
        heapq.heappush(self.n[number],index)

    def find(self, number: int) -> int:
        while self.n[number]:
            i=self.n[number][0]
            if self.c[i]==number: return i
            heapq.heappop(self.n[number])
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
