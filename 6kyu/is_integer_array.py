# Write a function with the signature shown below:

# def is_int_array(arr):
#     return True
# returns true / True if every element in an array is an integer or a float with no decimals.
# returns true / True if array is empty.
# returns false / False for every other input.

def is_int_array(arr):
    good_list = []
    if arr == []:
        return True
    if arr:
        for n in arr:
            if type(n) == int:
                good_list.append(n)
            if type(n) == float and n - round(n) == 0:
                good_list.append(n)
        if len(good_list) == len(arr):
            return True
    return False


print(is_int_array([1, 2, 3, 4]))


# test.assert_equals(is_int_array([]), True, "Input: []")
# test.assert_equals(is_int_array([1, 2, 3, 4]), True, "Input: [1, 2, 3, 4]")
# test.assert_equals(is_int_array([-11, -12, -13, -14]), True, "Input: [-11, -12, -13, -14]")
# test.assert_equals(is_int_array([1.0, 2.0, 3.0]), True, "Input: [1.0, 2.0, 3.0]")
# test.assert_equals(is_int_array([1, 2, None]), False, "Input: [1,2, None]")
# test.assert_equals(is_int_array(None), False, "Input: None")
# test.assert_equals(is_int_array(""), False, "Input: ''")
# test.assert_equals(is_int_array([None]), False, "Input: [None]")
# test.assert_equals(is_int_array([1.0, 2.0, 3.0001]), False, "Input: [1.0, 2.0, 3.0001]")
# test.assert_equals(is_int_array(["-1"]), False, "Input: ['-1']")