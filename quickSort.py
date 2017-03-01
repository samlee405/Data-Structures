# define the absolute worst version of the problem
#
# hey, help me out by checking out this app
# hey, you may get something awesome out of this

# message people individually. look for 100 sample size.
# "hey, i just got this new musci from your library. thanks. check out the app."

def quickSort(array, left, right):
    # base case
    if right < left:
        return

    pivot = array[right]

    low = left
    high = right - 1

    while low <= high:
        while array[low] <= pivot and low <= high:
            low += 1

        while array[high] >= pivot and low <= high:
            high -= 1

        if high < low:
            break

        if array[low] > array[high]:
            print("switching " + str(array[low]) + " and " + str(array[high]))
            array[low], array[high] = array[high], array[low]
            print(array)

    array[right], array[low] = array[low], array[right]
    print(array)

    print(left)
    print(high - 1)
    quickSort(array, left, high - 1)
    # quickSort(array, high + 1, right)

if __name__ == "__main__":
    unsortedArray = [2, 4, 7, 1, 13, 5]
    # sortedArray = [5, 7, 1, 13, 3].sort()

    print(unsortedArray)
    quickSort(unsortedArray, 0, len(unsortedArray) - 1)
    # print(sortedArray)
