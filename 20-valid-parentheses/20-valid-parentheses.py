class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        open = ["(", "[", "{"]
        close = [")", "]", "}"]
        pair = ["()", "[]", "{}"]
        
        for i in s:
            if i in open:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if stack.pop()+i in pair:
                    pass
                else:
                    return False
                
        if len(stack) == 0:
            return True
        else:
            return False