class Solution:
    def countAndSay(self, n: int) -> str:
        # base condition
        if n==1:
            return "1"
        else:
            # get the previous value
            n1 = self.countAndSay(n-1)
            soln =""
            # iterate for every character and modify result accordingly
            for i in range(len(n1)):
                # if the result equals previous character, keep adding 1
                if i>0 and n1[i]==n1[i-1]:
                    soln=soln[:-2]+(str(int(soln[-2])+1)+n1[i])
                # in all other cases, we append a new entry for the character
                else:
                    soln+=("1"+n1[i])
            return soln