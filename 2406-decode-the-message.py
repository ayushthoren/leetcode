class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
      code={}
      iSkipped=0
      for i in range(len(key)):
        if key[i] not in code and key[i].isalpha(): code[key[i]]=chr(97+(i-iSkipped))
        else: iSkipped+=1
      decode=""
      for j in message:
        if j in code: decode+=code[j]
        else: decode+=j
      return decode
