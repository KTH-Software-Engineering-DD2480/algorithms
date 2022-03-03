"""
Atbash cipher is mapping the alphabet to it's reverse.
So if we take "a" as it is the first letter, we change it to the last - z.

Example:
Attack at dawn --> Zggzxp zg wzdm

Complexity: O(n)
"""

def atbash(s):
    """Returns the inverse of input s"""

    translated = ""
    for i in s:
        n = ord(i)

        if i.isalpha():

            if i.isupper():
                x = n - ord('A')
                translated += chr(ord('Z') - x)

            if i.islower():
                x = n - ord('a')
                translated += chr(ord('z') - x)
        else:
            translated += i
    return translated
