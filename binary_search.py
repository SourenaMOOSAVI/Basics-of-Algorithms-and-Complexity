def binary_search(arr, ele):
    """
    A binary search function that finds the existence/nonexistence
    of an element in a sorted list"""

    # Defining the first and last index values
    first = 0
    last = len(arr) - 1
    
    while first <= last:

        # Set the midpoint
        mid = (first+last) // 2

        if arr[mid] == ele: # Match found
            return mid
        elif ele < arr[mid]:
            last = mid - 1
        else:
            first = mid + 1

    return -1  # Element not found

# Tasting our algorithm
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(binary_search(arr,13))
print(binary_search(arr,4))


def rec_bin_search(arr, ele, first=0, last=None):
    """
    A recursive binary search algorithm"""

    if last is None:
        last = len(arr) - 1

    if first > last:
        return -1  # Element not found

    mid = (first + last) // 2

    if arr[mid] == ele:
        return mid  # Return index
    elif ele < arr[mid]:
        return rec_bin_search(arr, ele, first, mid - 1)
    else:
        return rec_bin_search(arr, ele, mid + 1, last)

# Tasting our algorithm
print(rec_bin_search(arr, 19))