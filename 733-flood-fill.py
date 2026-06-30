class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        o = image[sr][sc]
        if color == o: return image
        q = deque()

        def change(y, x):
            q.append((y, x))
            image[y][x] = color

        change(sr, sc)

        while q:
            y, x = q.popleft()

            if y-1 >= 0 and image[y-1][x] == o: change(y-1, x)
            if y+1 < len(image) and image[y+1][x] == o: change(y+1, x)
            if x-1 >= 0 and image[y][x-1] == o: change(y, x-1)
            if x+1 < len(image[y]) and image[y][x+1] == o: change(y, x+1)

        return image
