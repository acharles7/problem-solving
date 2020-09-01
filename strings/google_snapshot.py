from collections import Counter

def frequecy_map(word):
    return sorted(Counter(word).items(), key = lambda pair: pair[0])

def compare_frequency(a_list, b_list):
    len_small = len(a_list) if len(a_list) <= len(b_list) else len(b_list)
    for i in range(len_small):
        if a_list[i][1] > b_list[i][1]:
            return True
    return len(a_list) > len(b_list)

def list_frequency(words):
    list_word = words.split(' ')
    list_word_freq = []
    for word in list_word:
        list_word_freq.append(frequecy_map(word))
    return list_word_freq

def compare(A, B):
    return_array = []
    array_a_freq = list_frequency(A)
    array_b_freq = list_frequency(B)
    for b_word_freq in array_b_freq:
        counter = 0
        for a_word_freq in array_a_freq:
            if compare_frequency(b_word_freq, a_word_freq):
                counter += 1
        return_array.append(counter)
    print(return_array)

A = 'abcd aabc bd'
B = 'aaa aa'
compare(A, B)
