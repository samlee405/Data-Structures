#!python

import string

<<<<<<< HEAD
=======

>>>>>>> 57a2bb60aaca1cc4f561a776601dc8c66e8f20f4
def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing"""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str)
<<<<<<< HEAD
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)

def is_palindrome_iterative(text):
    text = cleanText(text)

    characterIndex = 0
    while characterIndex < (len(text) / 2):
        if text[characterIndex] != text[-(characterIndex + 1)]:
            return False

        characterIndex += 1

    return True

def is_palindrome_recursive(text, left=None, right=None):
    if left == None:
        text = cleanText(text)
        print(text)

        if len(text) == 0 or len(text) == 1:
            return True

        left = 0
        right = len(text) - 1

    # print(left)
    # print(right)
    if text[left] != text[right]:
        return False
    elif left >= right and text[left] == text[right]:
        return True
    else:
        return is_palindrome_recursive(text, left + 1, right - 1)

def is_contained_in(substring, string):
    left = 0
    right = len(substring)

    while right <= (len(string)):
        if substring == string[left:right]: # not space efficient
            return True

        left += 1
        right += 1

    return False

def is_anagram(text, text2):
    setA = set(cleanText(text))
    setB = set(cleanText(text2))

    if setA <= setB and setA >= setB:
        return True
    else:
        return False

def cleanText(text):
    text = text.replace(" ", "")
    text = text.replace("!", "")
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("?", "")
    text = text.replace("\'", "")
    text = text.replace("-", "")
    text = text.lower()
    return text
=======
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    pass
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    pass
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests

>>>>>>> 57a2bb60aaca1cc4f561a776601dc8c66e8f20f4

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            str_not = 'a' if is_pal else 'not a'
            print('{}: {} is {} palindrome'.format(result, repr(arg), str_not))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
<<<<<<< HEAD
    # main()

    # print(is_contained_in("in", "thing"))
    print(is_anagram("Debit card", "Bad credit"))
=======
    main()
>>>>>>> 57a2bb60aaca1cc4f561a776601dc8c66e8f20f4
