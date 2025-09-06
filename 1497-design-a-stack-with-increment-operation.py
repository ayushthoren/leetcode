class CustomStack:

    def __init__(self, maxSize: int):
        self.ms = maxSize
        self.s = []

    def push(self, x: int) -> None:
        if len(self.s) < self.ms: self.s.append(x)
        
    def pop(self) -> int:
        return self.s.pop() if self.s else -1
        
    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.s))): self.s[i] += val
        
# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
