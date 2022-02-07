class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_int = ''
        for i in digits:
            digits_int += str(i)
        digits_int = str(int(digits_int)+1)
        digits_list = [int(i) for i in digits_int]
        return digits_list
        