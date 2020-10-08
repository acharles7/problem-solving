"""
Given a chemical formula (given as a string), return the count of each atom.
Leetcode 726. Number of Atoms
"""

def count_atoms(formula):    
    stack = [{}]
    i, n = 0, len(formula)

    while i < n:

        if formula[i] == '(':
            stack.append({})
            i += 1

        elif formula[i] == ')':
            last = stack.pop()
            i += 1

            digit = ''
            while i < n and formula[i].isdigit():
                digit += formula[i]
                i += 1

            digit = int(digit) if digit else 1

            for ele, val in last.items():
                if ele in stack[-1]:
                    stack[-1][ele] += val*digit 
                else:
                    stack[-1][ele] = val*digit

        else:
            name = formula[i]
            i += 1
            while i < n and formula[i].islower():
                name += formula[i]
                i += 1

            digit = ''
            while i < n and formula[i].isdigit():
                digit += formula[i]
                i += 1

            digit = int(digit) if digit else 1

            if name not in stack[-1]:
                stack[-1][name] = digit
            else:
                stack[-1][name] += digit

    sorted_atom = sorted(stack[0].items(), key=lambda l:l[0])
    return ''.join(key+str(val) if val > 1 else key for key, val in sorted_atom)


formula = "K4(ON(SO3)2)2"
count_atoms(formula)

