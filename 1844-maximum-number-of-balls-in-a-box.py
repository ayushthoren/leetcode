class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes={}
        for i in range(lowLimit,highLimit+1):
            summ=sum([int(j) for j in str(i)])
            if summ not in boxes: boxes[summ]=0
            boxes[summ]+=1
        return max(boxes.values())
