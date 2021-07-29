# Complete the solution so that the function will break up camel casing, using a space between words.
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""


def solution(s):
    # Declare empty string to eventually hold result.
    final_string = ""

    # loop through each character in the string. If char is uppercase, 
    # add to final string with a space before it. Else add lowercase char to final_string.
    for i in range(len(s)):
        char = s[i]
        if char.isupper():
            final_string += " " + char
        else:
            final_string += char
    return final_string


print(solution("camelCaseWord"))