"""
HeapSort
Runtime complexity O(N LogN)
Space complexity O(N)
"""

# heapify is O(Logn)
def heapify(arr, n, parent):

    largest = parent
    left = 2 * parent + 1
    right = 2 * parent + 2
 
    if left < n and arr[largest] < arr[left]:
        largest = left
 
    if right < n and arr[largest] < arr[right]:
        largest = right
 
    if largest != parent:
        arr[parent], arr[largest] = arr[largest], arr[parent]
        heapify(arr, n, largest)
 
 
def heapSort(arr):
    n = len(arr)

    #time complexity is O(n)
    for i in range( n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # time complexity is O(nlogn)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    
    return arr
 
 
"""
Test HeapSort
Generate a maximum of 10 random numbers.

Can we implement this in place?
"""

import random

for i in range(5):
    unsorted = []
    
    for i in range(10):
        unsorted.append(random.randint(0,100))
    
    sorted_list = heapSort(unsorted)
    print(unsorted, "->", sorted_list)
    assert( sorted_list == sorted(unsorted))
    