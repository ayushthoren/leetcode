class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
      dupes=[]
      cts={}
      for i in range(len(s)-9):
        section=s[i:i+10]
        if section not in cts: cts[section]=0
        cts[section]+=1
        if cts[section]>1: dupes.append(section)
      return list(set(dupes))
