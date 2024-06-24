class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: return False
        rev,tmp=0,x
        while tmp!=0: rev=(rev*10)+(tmp%10); tmp//=10
        return rev==x