def binary_search(arr, ele):
    """
    A binary search function that finds the existence/nonexistence
    of an element in a sorted list"""

    # Defining the first and last index values
    first = 0
    last = len(arr)-1

    found = False

    
    while first <= last and not found:

        # Set the midpoint
        mid = (first+last)//2

        # Match found
        if arr[mid] == ele:
            found = True
        
        # Set new midpoints up or down depending on the comparison
        else:
            # Set down
            if ele < arr[mid]:
                last = mid-1
            # Set up
            else:
                first = mid+1
    
    return found

# Tasting our algorithm
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(binary_search(arr,13))
print(binary_search(arr,4))



def rec_bin_search(arr, ele):
    """
    A recursive binary search algorithm"""

    # Base case
    if len(arr) == 0:
        return False

    # Recursive case
    else:

        mid = len(arr)//2

        # If match found
        if arr[mid] == ele:
            return True
        else:
            
            # Call again on second half
            if ele < arr[mid]:
                return rec_bin_search(arr[:mid],ele)
            
            # Or call on first half
            else:
                return rec_bin_search(arr[mid+1:], ele)

# Tasting our algorithm
print(rec_bin_search(arr, 19))