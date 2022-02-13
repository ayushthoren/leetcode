class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
      #For each number within the range of the given number...
      for i in range(1, n):
        #If the current number doesn't have zero, and
        #The number that can be added to it to make the given number doesn't have one, 
        #Return those two numbers
        if "0" not in str(i) and "0" not in str(n-i): return [i, n-i]
