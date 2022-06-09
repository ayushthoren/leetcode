class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
      letters, target=[ord(c) for c in letters], ord(target)
      for i in letters:
        if i>target: return chr(i)
      return chr(letters[0])
