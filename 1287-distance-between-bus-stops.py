class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
      p1,p2=start,start
      forwards,backwards=0,0
      while p1!=destination:
        forwards+=distance[p1]
        p1+=1
        if p1>len(distance)-1: p1=0
        # print(f'forwards is {forwards}')
      while p2!=destination:
        p2-=1
        if p2<0: p2=len(distance)-1
        backwards+=distance[p2]
        # print(p2)
      # print(forwards, backwards)
      return min([forwards, backwards])
