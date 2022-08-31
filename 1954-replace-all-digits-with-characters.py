class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        new=""
        for i in range(len(s)):
            if s[i].isnumeric(): new+=chr(ord(s[i-1])+int(s[i]))
            else: new+=s[i]
        return new
