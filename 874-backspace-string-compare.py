class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(txt):
            st=[]
            for i in txt:
                if i=="#":
                    if st: st.pop()
                else: st.append(i)
            return st
        return helper(s)==helper(t)
