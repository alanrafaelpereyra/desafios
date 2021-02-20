
"""
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
"""


def generate_hashtag(texto):
    if len(texto)>140 or len(texto)==0:   #making sure that garbage dont get in the function
        return False
    else:
        abc=texto.split()                #getting a list without spaces
        mayus=[i.capitalize() for i in abc]    
        mayus.insert(0,'#')    
        mayus2=''.join(mayus)           #getting all elements together in a string
    return mayus2




