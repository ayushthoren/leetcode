class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        return (s := set(friends)) and [i for i in order if i in s]
