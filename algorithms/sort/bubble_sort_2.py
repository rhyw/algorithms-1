#!/usr/bin/env python


def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    list_length = len(arr)

    # Perform sort
    j = 0
    # j is the loop number needed to get an array sorted.
    for j in range(list_length-2):
        for i in range(list_length-1):
            if arr[i] > arr[i+1]:
                swap(i, i+1)
        print('Round {}: {}'.format(j+1, arr))

    return arr


if __name__ == "__main__":
    arr = [1, 8, 5, 2, 3, 21, 13, 55, 34, 89, 1]
    sorted_arr = bubble_sort(arr)
    print('Array after bubble sort: {}'.format(sorted_arr))
