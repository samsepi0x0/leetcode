class Solution:
    def longestPalindrome(self, s: str) -> str:
        if (self.isPalin(s)):
            return s;
        palin = ""
        temp = ""
        for i in range(0, len(s) - 1):
            temp += s[i]
            for j in range(i+1, len(s)):
                temp += s[j]
                if(self.isPalin(temp)):
                    if(len(temp) > len(palin)):
                        palin = temp
            temp = ""
        if palin == "":
            return "" + s[0]
        return palin
    def isPalin(self, s: str) -> bool:
        return s == s[::-1]
