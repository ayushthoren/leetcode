class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        d={pieces[i][0]:i for i in range(len(pieces))}
        new=[]
        for j in arr:
            if j in d: new.extend(pieces[d[j]])
        return new==arr
