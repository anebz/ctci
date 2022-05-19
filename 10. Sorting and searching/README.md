# 10. Sorting and searching

## Sorting algorithms

### Bubble sort

> Runtime O(n<sup>2</sup>) average and worst case. Memory O(1)

Start at the beginning, swap the first two elements if the first is greater than the second. Go to the next pair and repeat, and so on until reaching the end of the array.

```python
nums = [2, 1, 4, 6, 3, 8, 0]
for k in range(len(nums)-1):
    for i in range(len(nums) - k - 1):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
```

### Selection sort

> Runtime O(n<sup>2</sup>) average and worst case. Memory O(1)

Simple but inefficient. Find the smallest element using a linear scan, move it to the front, swapping it with the first element. Then, find the second smallest and move it, doing a linear scan. And so on.

```python
nums = [2, 1, 4, 6, 3, 8, 0]
for i in range(len(nums)):
    min_pos = i
    for j in range(i+1, len(nums)):
        if nums[j] < nums[min_pos]:
            min_pos = j
    nums[i], nums[min_pos] = nums[min_pos], nums[i]
```

### Merge sort

> Runtime O(n log(n)) average and worst case. Memory depends, usually O(n)

Divides the array in half, sort each of these halves, merge them back together. Eventually, you merge just the two single-element arrays, and the merge part does all the heavy lifting.

When merging, copy all the elements from the target array segment into a helper array, when iterating through helper, copy the smaller element from each half into the array. At the end, copy any remaining elements into the target array.

Java algorithm in book.

```python
def merge_sort(arr):
    if len(arr) > 1:

        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    
    return arr
```

### Quick sort

Similar to merge sort, divide and conquer.

> Runtime O(n log(n)) average, O(n<sup>2</sup>) worst case. Memory O(n log(n))

Pick a random element and partition the array, such that all numbers lower than the partitioning element come before all elements greater than it. Repeatedly partitioning the array (and its sub-arrays) around an element, the array is eventually sorted. But as the partitioned element is not guaranteed to be the median or close to it, the sorting could be very slow. That is why the worst case rutime is O(n<sup>2</sup>).

```pseudocode
a = [3, 5, 2, 4, 1, 6, 7], left=0, right=6

pivot = a[3] = 4

left = 1
right = 4

swap a
a = [3, 1, 2, 4, 5, 6, 7]
left = 2
right = 3

next loop of big while
left = 3
right = 3

swap a
remains the same because left=right
left = 4
right = 2

break big loop, return 4 -> index=4

left=0 < index-1=3, so quicksort the left half
index=4 < right=6, so quicksort the right half
```

### Radix sort

> Runtime O(kn)

Sorting algorithm for integers that takes advantage of the fact that integers have a finite number of bits. We iterate through each digit of the number, grouping numbers by each digit. With an array of integers, we might sort by the first digit, so that the 0s are grouped together, then sort by the next digit.

N is the number of elements and k is the number of passes of the sorting algorithm.

### [Bucket sort](https://en.wikipedia.org/wiki/Bucket_sort)

> Runtime O(n<sup>2</sup>) worst case, O(n + n<sup>2</sup>/k + k) where k is the number of buckets, average performance. Worst-case space complexity is O(nk)

This is a sorting algorithm that distributes the elements of an array into a number of buckets. Each bucket is sorted individually, either using a different sorting algorithm or by recursively applying the bucket sorting algorithm.

## Searching algorithms

In **binary search**, we look for an element x in a sorted array by first comparing x to the midpoint of the array. If x is lower, we search the left half. and vice versa.

See code in book, see below for Python:

```python
def binarySearch(arr, x):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
  
        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1
        # If x is smaller, ignore right half
        else:
            r = mid - 1
    return -1

arr = [2, 3, 4, 10, 40]
x = 10
result = binarySearch(arr, x)
```

There are more algorithms than just binary search, use binary trees or hash tables too.
