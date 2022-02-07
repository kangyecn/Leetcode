import math
class Solution:
    def climbStairs(self, n: int) -> int:
       phi = ((1 + math.sqrt(5)) / 2)
       psi = ((1 - math.sqrt(5)) / 2)
       return int((pow(phi,n+1) - pow(psi,n+1))/math.sqrt(5))