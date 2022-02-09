class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d={ '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']}
        if len(digits)==0:
            return []
        soln=d[digits[0]]
        
        for k in range(1,len(digits)):
            soln=[i+j for i in soln for j in d[digits[k]]]
        return soln