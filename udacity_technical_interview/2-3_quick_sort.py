"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def quicksort(array):
    pivot_position = len(array) - 1
    if pivot_position < 1:
        return array
    pivot = array[pivot_position]
    counter = 0
    while counter < pivot_position:
        if array[counter] > pivot:
            array[pivot_position] = array[counter]
            array[counter] = array[pivot_position - 1]
            array[pivot_position - 1] = pivot
            pivot_position -= 1
        else:
            counter += 1
    array[0:pivot_position] = quicksort(array[0:pivot_position])
    array[pivot_position:len(array)] = quicksort(array[pivot_position:len(array)])
    return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
