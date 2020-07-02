def single_multiply(num_x, num_y, o):
    out, carry = '', 0
    for i in range(len(num_x)-1, -1, -1):
        temp = int(num_x[i])*int(num_y)
        if carry > 0:
            temp = str(temp + carry)
        else:
            temp = str(temp)
        if len(temp) > 1:
            out += str(temp[1])
            carry = int(temp[0])     
        else:
            out += str(temp[0])
            carry = 0

    if carry > 0:
        return str(carry) + out[::-1] + (o*'0')
    return out[::-1]+ (o*'0')

def add_to_res(res, string):
    if len(res) < len(string):
        diff = len(string) - len(res)
        res = '0'*diff + res
    else:
        diff = len(res) - len(string)
        string = '0'*diff + string

    carry, out = 0, ''
    for i in range(len(res)-1, -1, -1):
        temp = int(res[i]) + int(string[i])
        if carry > 0:
            temp = str(temp + carry)
        else:
            temp = str(temp)
        
        if len(temp) > 1:
            out += str(temp[1])
            carry = int(temp[0])
        else:
            out += str(temp[0])
            carry = 0
        
    if carry > 0:
        return str(carry) + out[::-1]
    return out[::-1]
    
def multiply(num1: str, num2: str) -> str:
    out, res = [], ''
    for i, j in enumerate(reversed(num2)):
        out.append(single_multiply(num1, j, i))
    for i in range(len(out)):
        res = add_to_res(res, out[i])
    return res

if __name__ == '__main__':
    num1 = "123456789"
    num2 = "987654321"
    print(multiply(num1, num2))
