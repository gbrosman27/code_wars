# Step 1: Create a function called encode() 
# to replace all the lowercase vowels in a given string with numbers 
# according to the following pattern:
# For example, encode("hello") would return "h2ll4". There is no need to worry about uppercase vowels in this kata.
# Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern shown above.
# For example, decode("h3 th2r2") would return "hi there".
# For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.


vowels = {"a": 1, "e": 2, "i": 3, "o": 4, "u": 5}

# If the vowels exist in the passed in string, change those vowels to the correct value.
def encode(st):
    new_word = st
    for vowel in vowels.keys():
        if vowel in new_word:
            new_word = new_word.replace(vowel, str(vowels[vowel]))
    return new_word
        

# If the passed in string contains a number that also corresponds to a vowel in the above dictionary, replace the number with the correct vowel.
def decode(st):  
    reg_word = st
    for key, val in vowels.items():
        if str(val) in reg_word:
            reg_word = reg_word.replace(str(val), str(key))
    return reg_word   


print(encode('hello world'))
print(decode('h2ll4 w4rld'))