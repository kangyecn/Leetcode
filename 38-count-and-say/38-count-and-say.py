class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        else:
            n1 = self.countAndSay(n-1)
            soln =""
            for i in range(len(n1)):
                if i>0 and n1[i]==n1[i-1]:
                    soln=soln[:-2]+(str(int(soln[-2])+1)+n1[i])
                else:
                    soln+=("1"+n1[i])
            return soln