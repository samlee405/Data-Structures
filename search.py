#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests below

    if index < 0 or not isinstance(index, int):
        raise ValueError
    elif index > len(array) - 1:
        return None
    elif array[index] == item:
        return index
    else:
        return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests below

    lowerIndex = 0
    upperIndex = len(array) - 1

    while lowerIndex <= upperIndex:
        middleIndex = (lowerIndex + upperIndex) / 2
        if array[middleIndex] == item:
            wasFound = True
            return middleIndex
        elif array[middleIndex] > item:
            upperIndex = middleIndex - 1
        elif array[middleIndex] < item:
            lowerIndex = middleIndex + 1

    return None

def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests below

    if left == None:
        left = 0
        right = len(array) - 1

    if len(array) == 0 or left > right:
        return None

    middle = (left + right) / 2
    if array[middle] == item:
        return middle
    elif array[middle] < item:
        return binary_search_recursive(array, item, middle + 1, right)
    elif array[middle] > item:
        return binary_search_recursive(array, item, left, middle - 1)
