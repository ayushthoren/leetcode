class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        #For each letter i nthe strign with the added character
        for i in t:
            #If the curretn letter was added to t, return it
            if t.count(i)!=s.count(i): return i
