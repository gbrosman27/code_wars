# Complete the solution so that the function will break up camel casing, using a space between words.
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

def solution(camelCase):
    # loop through string and find uppercase. split on uppercase.
    for char in camelCase:
        if char.isupper():  
            result = camelCase.split(char)
            
            return result



print(solution("camelCase"))

# first = camelCase[:index]
# second = camelCase[index:]