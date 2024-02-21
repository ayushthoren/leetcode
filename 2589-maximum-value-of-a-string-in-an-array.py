class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        return max([int(i) if i.isnumeric() else len(i) for i in strs ])
