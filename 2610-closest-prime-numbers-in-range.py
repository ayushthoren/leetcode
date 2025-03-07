class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def prime(n):
            if n==1: return False
            for d in range (2,n//2+1):
                if n%d==0: return False
            return True

        primes,ct,step=[],0,1
        if left<2: primes.append(2)
        if left%2==1: step=2
        else: left+=1
        for i in range(left,right+1,step):
            if prime(i):
                if primes and i-primes[-1]<=2: return [primes[-1],i]
                primes.append(i); ct+=1

        if ct<2: return [-1,-1]
        m,ans=primes[-1],[]
        for j in range(ct-1):
            diff=primes[j+1]-primes[j]
            if diff<m:
                m=diff
                ans=[primes[j],primes[j+1]]
        return ans
