class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        return sum(numerals[s[i]]*(-1)**(numerals[s[i]]<numerals[s[i+1]]) for i in range(len(s)-1)) + numerals[s[-1]]