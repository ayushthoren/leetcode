class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence=sentence.split(" ")
        sl=len(sentence)
        for i in range(sl):
            if i==sl-1:
                if sentence[i][-1]!=sentence[0][0]: return False
            elif sentence[i][-1]!=sentence[i+1][0]: return False
        return True
