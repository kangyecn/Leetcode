class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = 0
        sign = (dividend < 0) ^ (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        for i in range(31,-1,-1):
            if divisor * (1 << i) <= dividend:
                ans = ans | (1 << i)
                dividend = dividend - (divisor * (1 << i))
        if sign == True:
            ans = -1 * ans
        return ans if ans <= (2 ** 31) - 1 else (2 ** 31) - 1