class Solution:
    def generateTag(self, caption: str) -> str:
        return "#" + "".join([w.capitalize() if i else w.lower() for i, w in enumerate(caption.split())])[:99]
