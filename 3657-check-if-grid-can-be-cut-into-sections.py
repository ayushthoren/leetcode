class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        cx,cy=0,0
        rx,ry=sorted(rectangles,key=lambda x: x[0]),sorted(rectangles,key=lambda y: y[1])
        fx,fy=rx[0][2],ry[0][3]
        for x1,_,x2,_ in rx:
            if x1>=fx: cx+=1
            fx=max(fx,x2)
        for _,y1,_,y2 in ry:
            if y1>=fy: cy+=1
            fy=max(fy,y2)
        return cx>=2 or cy>=2
