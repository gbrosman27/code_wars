# There is an array with some numbers. All numbers are equal except for one. Try to find it!
# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.
# The tests contain some very huge arrays, so think about performance.


# Convert the array to a set to eliminate multiple same numbers. For each number in the set, 
# if the number appears exactly one time in the original array, that is the answer.
def find_uniq(arr):
    unique = set(arr)
    for num in unique:
        if arr.count(num) == 1: 
            return num


print(find_uniq([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 3, 10, 10, 10, 10]))


# All 61 tests passed.