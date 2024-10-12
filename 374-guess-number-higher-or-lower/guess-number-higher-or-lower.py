# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

import random

class Solution:
    def guessNumber(self, n: int) -> int:
        minn=1
        maxx=n
        guessNum=random.randint(minn, maxx)
        result=guess(guessNum)
        while result!=0:
            if result==1: minn=guessNum
            if result==-1: maxx=guessNum
            guessNum=random.randint(minn, maxx)
            result=guess(guessNum)
        return guessNum