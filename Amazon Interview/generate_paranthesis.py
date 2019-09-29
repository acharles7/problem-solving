def generateParenthesis(n: int):
    ans = []
    def backtrack(S = '', left = 0, right = 0):
        print(S)
        if len(S) == 2*n:
            ans.append(S)
            return
        if left < n:
            backtrack(S+'(', left+1, right)
        if right < left:
            backtrack(S+')', left, right+1)

    backtrack()
    return ans
n = 3
print(generateParenthesis(n))
