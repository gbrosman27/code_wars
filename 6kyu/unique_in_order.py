# Implement the function unique_in_order which takes as argument a sequence and returns a list of items 
# without any elements with the same value next to each other and preserving the original order of elements.

# For example:
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]


# def unique_in_order(iterable):
#     uniques_list = []
#     for x in iterable:
#         if x not in uniques_list:
#             uniques_list.append(x)
#     print(uniques_list)


# Append the char to the list if not already in the list, and if char does not equal the previous. 
# Make variable prev equal to the char that was just added so that it isn't added again.
def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable:
        if char != prev:
            result.append(char)
            prev = char
    print(result)

unique_in_order('ABBCcAD')
        