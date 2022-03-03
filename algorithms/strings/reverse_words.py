"""
Reverse the words in a string

Example 1:
Input: I am keon kim and I like pizza
Output: pizza like I and kim keon am I
"""

def reverse(array, i, j):
    while i < j:
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1


def reverse_words(string):
    """
    :type s: str
    :rtype: str
    """
    arr = string.strip().split()  # arr is list of words
    n = len(arr)
    reverse(arr, 0, n-1)

    return " ".join(arr)


if __name__ == "__main__":
    test = "I am keon kim and I like pizza"
    print(test)
    print(reverse_words(test))
