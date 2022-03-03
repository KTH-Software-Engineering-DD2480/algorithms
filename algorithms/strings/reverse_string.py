"""
Different ways to reverse a string
"""

def recursive(s):
    """
    :type s: str
    :rtype: str
    """
    l = len(s)
    if l < 2:
        return s
    return recursive(s[l//2:]) + recursive(s[:l//2])

def iterative(s):
    """
    :type s: str
    :rtype: str
    """
    r = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        r[i], r[j] = r[j], r[i]
        i += 1
        j -= 1
    return "".join(r)

def pythonic(s):
    """
    :type s: str
    :rtype: str
    """
    r = list(reversed(s))
    return "".join(r)

def ultra_pythonic(s):
    """
    :type s: str
    :rtype: str
    """
    return s[::-1]
