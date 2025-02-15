class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids=sorted(asteroids)
        for i in asteroids:
            if i>mass: return False
            mass+=i
        return True
