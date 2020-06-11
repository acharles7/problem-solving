def count_nine(num):
    NINE_POINT = 4
    nines = sum([1 for digit in num if digit == '9'])
    return nines*NINE_POINT
def consecutive_one(num):
    ONES_POINT = 5
    i = 0
    points = 0
    while i < len(num):
        if num[i] == '1':
            ones = 0
            while i < len(num) and num[i] == '1':
                ones += 1
                i += 1
                if ones == 2:
                    points += ONES_POINT
                elif ones > 2:
                    points += ONES_POINT
        else:
            i += 1
    return points    
def seven_multiple(num):
    return 1 if num % 7 == 0 else 0
def count_even(num):
    EVEN_POINT = 2
    evens = sum([1 for digit in num if digit in ('0', '2', '4', '6', '8')])
    return evens*EVEN_POINT
def find_sequence(num):
    groups = [[num[0]]] 
    for i in range(1, len(num)): 
        if int(num[i-1])+1 == int(num[i]): 
            groups[-1].append(num[i]) 
        else: 
            groups.append([num[i]]) 
    return sum([len(group)**2 for group in groups]) 
            
    
def number_score(num):
    nine = count_nine(str(num))
    print("Nine", nine)
    ones = consecutive_one(str(num))
    print("Ones", ones)
    sequence = find_sequence(str(num))
    print("Sequence", sequence)
    seven = seven_multiple(num)
    print("Seven", seven)
    even = count_even(str(num))
    print("Even", even)
    
    return sum([nine, ones, seven, even, sequence])
    
print("Total Points: ", number_score(29379985962))

