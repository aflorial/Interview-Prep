import random

"""
Big O & Notes 

Mergesort is a stable, out-of-place sorting algorithm

Time complexity of O(N log N)
Space complexity of O(N).

"""

def mergeSort(arr):

    if len(arr) == 1:
        return arr

    mid = len(arr) // 2

    left  = arr[mid:]
    right = arr[:mid]

    left = mergeSort(left)
    right = mergeSort(right)


    merged_arr = [0]*(len(left) + len(right))
    r_index = l_index = merged_index = 0

    while r_index < len(right) and l_index < len(left):

        if right[r_index] <= left[l_index]:
            merged_arr[merged_index] = right[r_index]
            r_index += 1
        else:
            merged_arr[merged_index] = left[l_index]
            l_index += 1
        
        merged_index += 1
    
    while r_index < len(right):
        merged_arr[merged_index] = right[r_index]
        r_index += 1
        merged_index += 1
    
    while l_index < len(left):
        merged_arr[merged_index] = left[l_index]
        l_index += 1
        merged_index += 1
    
    return merged_arr



"""
Test MergeSort
Generate a maximum of 10 random numbers.

Can we implement this in place?
"""

for i in range(5):
    unsorted = []
    for i in range(10):
        unsorted.append(random.randint(0,100))
    
    sorted_list = mergeSort(unsorted)
    assert( sorted_list == sorted(unsorted))
    print(unsorted, "->", sorted_list)




