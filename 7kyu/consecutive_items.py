def consecutive(arr, a, b):
    # If the index of a is 1 bigger or 1 lesser than the index of a, return True.
    if arr.index(a) == arr.index(b) - 1 or arr.index(a) == arr.index(b) + 1:
        return True
    return False


print(consecutive([1, 3, 5, 7],3,7))


# You are given a list of unique integers arr, and two integers a and b. 
# Your task is to find out whether or not a and b appear consecutively in arr, 
# and return a boolean value (True if a and b are consecutive, False otherwise).

# It is guaranteed that a and b are both present in arr.


# test.assert_equals(consecutive([1, 3, 5, 7], 3, 7), False)      
# test.assert_equals(consecutive([1, 3, 5, 7], 3, 1), True)    
# test.assert_equals(consecutive([1, 6, 9, -3, 4, -78, 0], -3, 4), True)