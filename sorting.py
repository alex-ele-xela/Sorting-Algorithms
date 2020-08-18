from time import time
from random import randrange

'''Insertion Sort below'''


def insertionSort(array):
    sortedArray = array[:]

    # Outer Array to iterate from 1th position to end position
    for i in range(1, len(sortedArray)):
        insertElement = sortedArray[i]

        # Inner Array to shift the insertElement back to required position
        j = i-1
        while (j >= 0 and insertElement < sortedArray[j]):
            sortedArray[j+1] = sortedArray[j]
            j -= 1
        sortedArray[j+1] = insertElement

    return sortedArray


'''Selection Sort below'''


def selectionSort(array):
    sortedArray = array[:]

    # Outer loop to place minimum element at required position
    for i in range(len(sortedArray)):

        # Calculating minimum element from i'th position till end and placing it at i
        minimum = i
        for j in range(i+1, len(sortedArray)):
            if sortedArray[j] < sortedArray[minimum]:
                minimum = j
        sortedArray[minimum], sortedArray[i] = sortedArray[i], sortedArray[minimum]

    return sortedArray


'''Bubble Sort below'''


def bubbleSort(array):
    sortedArray = array[:]

    # Outer loop which specifies the position to put the bubbled element
    for i in range(len(sortedArray)-1, 0, -1):

        # Loop for bubbling the greatest element to the i'th position
        for j in range(i):
            if sortedArray[j] > sortedArray[j+1]:
                sortedArray[j], sortedArray[j +
                                            1] = sortedArray[j+1], sortedArray[j]

    return sortedArray


'''Quick Sort below'''
# Function to partition array. It will partition the original passed array itself. low and high specify the start and end positions for partitioning


def partition(array, low, high):
    # Set pivot to the end element
    pivot = array[high]

    # Setting position for lesser elements
    i = low-1
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    # Now i stores the value of the last lesser element. We swap the next element with the pivot
    array[i+1], array[high] = array[high], array[i+1]

    # Now the pivot is stored in i+1
    return (i+1)

# Quick Sort Main


def quickSort(array, low=0, high=False):
    '''DO NOT pass the low and high arguments while calling the function to sort.
    Pass ONLY the array'''

    # Set high when the function is called the first time
    if type(high) == bool:
        array = array[:]
        high = len(array)-1

    # The concerned partition (low, high) is further sorted/partitioned only if low<high
    if low < high:
        pivot = partition(array, low, high)

        # The new partition are further sorted/partitioned
        quickSort(array, low, pivot-1)
        quickSort(array, pivot+1, high)

    return array


'''Merge Sort below'''
# Function to merge the given left and right parts


def merge(array, low, mid, high):
    # Making the left and right parts
    left = array[low:mid]
    right = array[mid:high+1]

    # Merging the left and right parts into a sorted array
    x = low
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[x] = left[i]
            i += 1
        else:
            array[x] = right[j]
            j += 1
        x += 1

    # Merging any leftovers
    while i < len(left):
        array[x] = left[i]
        i += 1
        x += 1

    while j < len(right):
        array[x] = right[j]
        j += 1
        x += 1

# Merge Sort Main


def mergeSort(array, low=0, high=0, recursion=False):
    '''DO NOT pass the low, high or recursion argument while calling the function to sort.
    Pass ONLY the array'''

    # Making a copy of the array on the first call by user, and setting high = last index = len(array)-1
    if not(recursion):
        array = array[:]
        high = len(array) - 1

    # Concerned part of array is divided and then merged only if its length > 1
    if low < high:
        # Getting position of middle element
        mid = (low + high + 1) // 2

        # Calling the mergeSort function for left and right parts
        mergeSort(array, low, mid-1, True)
        mergeSort(array, mid, high, True)

        # Merging the left and right parts
        merge(array, low, mid, high)

    return array


'''Functions to check the working of the algorithms below'''


def timeRecord(name, sortFunction, array):
    t1 = time()
    sortedArray = sortFunction(array)
    t2 = time()
    print(
        f"\nUsing {name} : {sortedArray}\nSorted {len(array)} elements in {t2-t1} seconds\n")


def main():
    n = int(input("Enter number of random elements to sort : "))
    array = [randrange(n) for i in range(n)]

    print("\nSorting", array)

    # Comment out the sorting algorithm that you don't want to check

    timeRecord("Bubble Sort", bubbleSort, array)

    timeRecord("Insertion Sort", insertionSort, array)

    timeRecord("Selection Sort", selectionSort, array)

    timeRecord("Quick Sort", quickSort, array)

    timeRecord("Merge Sort", mergeSort, array)


if __name__ == "__main__":
    main()
