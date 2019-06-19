#Extract maximum numeric value from a given string

def extractMaximum(S):
    num, res = 0, 0
    for i in range(len(S)):
        if(S[i] >= '0' and  S[i] <= '9'):
            num = num * 10 + int(S[i])
        else:
            res = max(res, num)
            num = 0
    return res

S = 'abchsd2031sdhs'
print(extractMaximum(S))
