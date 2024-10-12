class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        #For each letter in the strign with the added character
        for i in t:
            #If the current letter was added to t, return it
            if t.count(i)!=s.count(i): return i
