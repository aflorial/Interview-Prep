"""
Information about Sorting

https://medium.com/@mera.stackhouse/which-sorting-algorithms-to-know-for-the-tech-interview-654a1f619e1d
https://www.quora.com/Which-one-is-better-a-merge-sort-or-an-insertion-sort-Why
https://betterexplained.com/articles/sorting-algorithms/
https://courses.cs.washington.edu/courses/cse326/03wi/lectures/RaoLect16.pdf
https://www.geeksforgeeks.org/analysis-of-different-sorting-techniques/


Mergesort is a stable, out-of-place sorting algorithm with a time complexity of O(N log N)
and an extra space complexity of O(N).

Insertion sort is a stable, in place sorting algorithm with a time complexity of O(N²) and Ω(n). 
It doesn’t use any extra space.

Since insertion sort uses on average far fewer operations per single exchange,
it is more efficient for smaller (sub)arrays. You can resort to insertion sort
within merge sort to make merge sort more effective.

Your choice of sorting algorithm strongly depends on the data that needs to be sorted. 
As an example, for primitive data types, stable sorting algorithms only creates extra overhead 
and you should resort to using quicksort instead.

"""

