def get_difference(a, b):
    diff = [abs(i-j) for i, j in zip(a, b)]
    return diff, sum(diff)

        
def make_difference(a, b):
    min_diff = float('inf')
    base_diff_list, base_diff_sum = get_diff(a, b)
    
    for i in range(len(a)):
        new = a.copy()
        for j in range(len(a)):
            if  i == j:
                continue
            new[i] = new[j]
            
            base_diff_item = base_diff_list[i]
            item_diff = abs(new[i] - b[i])
            
            new_item_diff = base_diff_sum - base_diff_item + item_diff
            min_diff = min(min_diff, new_item_diff)
            
            print(new, new_item_diff, min_diff)
    return min(min_diff, base_diff_sum)

    
a, b = [1, 3, 5], [5, 3, 1]
make_difference(a, b)
