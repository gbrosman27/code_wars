# Sort the array regardless of capitalization.


def sortme(words):

    # Use the sorted function with the key parameter set to casefold. Sorts the array with case insensitivity.
    return sorted(words, key=str.casefold)


print(sortme(["C", "d", "a", "B"]))
print(sortme(["Hello", "there", "I'm", "fine"]))