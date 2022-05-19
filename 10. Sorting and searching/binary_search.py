# binary search in sorted array

# recursive
def binary_search_rec(nums, target, pos0, pos1):
    if pos0 <= pos1:
        midpoint = (pos0+pos1)//2
        if target == nums[midpoint]:
            return midpoint
        elif target > nums[midpoint]:
            return binary_search_rec(nums, target, midpoint+1, pos1)
        elif target < nums[midpoint]:
            return binary_search_rec(nums, target, pos0, midpoint-1)
    else:
        return -1

# iterative
def binary_search_iter(nums, target, pos0, pos1):
    while True:
        if pos0 <= pos1:
            midpoint = (pos0+pos1)//2
            if target == nums[midpoint]:
                return midpoint
            elif target > nums[midpoint]:
                pos0 = midpoint + 1
            elif target < nums[midpoint]:
                pos1 = midpoint - 1
        else:
            return -1

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 4
res = binary_search_iter(nums, target, 0, len(nums)-1)
print(res)  