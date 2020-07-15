
def find_it(seq):
    multiples = []
    for number in seq: 
        if seq.count(number) > 1 and seq.count(number) % 2 != 0:
            multiples.append(number)
    print(set(multiples))   


find_it([1, 1, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 7, 7, 7, 7, 7])