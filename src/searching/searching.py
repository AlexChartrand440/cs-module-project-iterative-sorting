def linear_search(arr, target):
    # Your code here

    index = 0;

    if len(arr) > 0:
        for i in arr:
            if i == target:
                return index;
            else:
                index += 1;

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    mid = 0;
    left = 0;
    right = len(arr) - 1;
  
    while left <= right: 
  
        mid = (right + left) // 2;

        if arr[mid] < target: 
            left = mid + 1;
        elif arr[mid] > target: 
            right = mid - 1;
        else: 
            return mid;
  
    return -1; # not found
