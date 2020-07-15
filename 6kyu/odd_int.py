# Given an array, find the integer that appears an odd number of times.


def find_it(seq):
    multiples = []
    for number in seq: 
        if seq.count(number) >= 1 and seq.count(number) % 2 != 0:
            multiples.append(number)
    new_set = set(multiples)
    new_list = list(new_set)
    str_list = ''.join(str(num) for num in new_list)
    print(int(str_list))
  

find_it([1, 1, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 7, 7, 7, 7, 7])