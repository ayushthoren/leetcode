class Solution:
    def trimMean(self, arr: List[int]) -> float:
        numRemove=len(arr)//20
        arr=sorted(arr)
        arr=arr[:-numRemove]
        arr=arr[numRemove:]
        return sum(arr)/len(arr)
