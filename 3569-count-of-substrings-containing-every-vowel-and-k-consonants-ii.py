class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels=set("aeiou")
        vct,cct={},0
        l=ct=valid=0

        def remove(c):
            if c in vowels:
                vct[c]-=1
                if vct[c]==0: del vct[c]
            else: nonlocal cct; cct-=1

        for r in word:
            if r in vowels: vct[r]=vct.get(r,0)+1
            else: cct+=1; ct=0
            while cct>k: remove(word[l]); l+=1
            while cct==k and len(vct)==5:
                ct+=1
                remove(word[l]); l+=1
            valid+=ct
        return valid
