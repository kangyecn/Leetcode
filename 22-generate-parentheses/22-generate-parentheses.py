class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(s, i, j):
            if i>n or j>n or j>i: return
            if len(s) == 2*n: result.append(s)
            dfs(s+"(", i+1, j)
            dfs(s+")", i, j+1)
        dfs('(', 1, 0)
        return result        