# An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
# Implement a function that determines whether a string that contains only letters is an isogram. 
# Assume the empty string is an isogram. Ignore letter case.

# is_isogram("Dermatoglyphics" ) == true
# is_isogram("aba" ) == false
# is_isogram("moOse" ) == false # -- ignore letter case

def is_isogram(string):
    # Convert to lower case. Change the string to a set so that each value appears only once. 
    # Take the length of the set. If length of original string == len of the new string, 
    # return True, it is an isogram.
    if len(string) == len(set(string.lower())):
        print(f"{string} is an isogram.")
    else:
        print(f"{string} is not an isogram.")

is_isogram("Dermatoglyphics")