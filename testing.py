from math import *
from test import make_anagram_dict

def histogram(x, y, width):
    dictionary = {}
    index = 1
    longest = 0
    for num in x:
        dictionary[num] = 0

    for key in H:
        if len(H[key]) > 1:
            dictionary[len(H[key])] += 1

    for i in dictionary:
        if dictionary[i] > longest:
            longest = dictionary[i]

    for number in dictionary:
        index += 1
        log_num = dictionary[number]
        if log_num > 0:
            log_num = log(log_num, 10)
            print(index, '*' * int(30 * (log_num / log(longest, 10))), log_num)

    return dictionary

if __name__ == "__main__":
    
    H = make_anagram_dict("words.txt")
    x = range(2, 13)

    y = histogram(x, H, width=20)
    print(y)