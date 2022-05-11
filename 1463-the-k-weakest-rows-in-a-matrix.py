class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
      cts={}
      weakest=[]
      for i in range(len(mat)):
        if mat[i].count(1) in cts: cts[mat[i].count(1)].append(i)
        else: cts[mat[i].count(1)]=[i]
      cts=dict(sorted(cts.items()))
      for d in cts: cts[d]=sorted(cts[d])
      for j in range(k):
        for l in cts:
          for o in cts[l]:
            if len(weakest)<k and o not in weakest: weakest.append(o)
      return weakest
