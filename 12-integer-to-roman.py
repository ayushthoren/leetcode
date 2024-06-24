class Solution:
    def intToRoman(self, num: int) -> str:
        parts,roman=[],""
        while num!=0: parts.append(num%10); num//=10
        parts=[parts[p]*(10**(p)) for p in range(len(parts))][::-1]
        for i in parts:
            if i%1000==0: roman+="M"*(i//1000); continue
            if i%100==0:
                hundct=i//100
                if hundct<=3: roman+="C"*hundct; continue
                if hundct==9: roman+="CM"; continue
                if hundct>=6: roman+="D"+("C"*(hundct-5)); continue
                if hundct==4: roman+="CD"; continue
                else: roman+="D"; continue
            if i%10==0:
                tensct=i//10
                if tensct<=3: roman+="X"*tensct; continue
                if tensct==9: roman+="XC"; continue
                if tensct>=6: roman+="L"+("X"*(tensct-5)); continue
                if tensct==4: roman+="XL"; continue
                else: roman+="L"; continue
            if i<=3: roman+="I"*i; continue
            if i==9: roman+="IX"; continue
            if i>=6: roman+="V"+("I"*(i-5)); continue
            if i==4: roman+="IV"; continue
            else: roman+="V"; continue
        return roman
