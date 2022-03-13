class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
      duration = {}
      for i in range(len(releaseTimes)):
        if i == 0: duration[keysPressed[i]] = releaseTimes[i]
        else:
          time = releaseTimes[i] - releaseTimes[i - 1]
          if keysPressed[i] in duration:
            if time>duration[keysPressed[i]]:
              duration[keysPressed[i]] = time
          else:
              duration[keysPressed[i]] = time
      highestDuration = max(duration.values())
      letters=[j for j in duration if duration[j]==highestDuration]
      return sorted(letters)[-1]
