# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

def get_count(input_str):
    a=input_str.count('a')
    e=input_str.count('e')
    i=input_str.count('i')
    o=input_str.count('o')
    u=input_str.count('u')
    num_vowels = a+e+i+o+u
    
    
    return num_vowels

"""
input_str='Hola'

print(total)
"""
