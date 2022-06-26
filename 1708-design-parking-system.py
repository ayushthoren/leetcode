class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big=big
        self.medium=medium
        self.small=small

    def addCar(self, carType: int) -> bool:
        BIG, MEDIUM, SMALL = 1, 2, 3
        if carType == BIG and self.big > 0:
          self.big-=1
          return True
        elif carType == MEDIUM and self.medium > 0:
          self.medium-=1
          return True
        elif carType == SMALL and self.small > 0:
          self.small-=1
          return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
