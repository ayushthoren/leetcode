class RecentCounter:

    def __init__(self):
        self.requests = []
        self.i = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[self.i] < t - 3000: self.i += 1
        return len(self.requests) - self.i


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
