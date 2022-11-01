def seq_search(arr, ele):
    """
    A basic sequantial (linear) search algorithm for an unordered list
    Returns True if the element is found and False otherwise"""

    # Start the search at position/index 0
    pos = 0
    # Target becomes true if the ele is in the list
    found = False

    # Iterate until the end of the list
    while pos < len(arr) and not found:
        
        # If matched retrun True
        if arr[pos] == ele:
            found = True
        # Else move to the next element
        else:
            pos += 1

    return found

# Testing the algorithm
arr = [13, 8, 2, 11, 3, 4, 17, 5, 60]

print(seq_search(arr,11))
print(seq_search(arr,10))


def orederd_seq_search(arr, ele):
    """
    A general sequantial (linear) search algorithm for an ordered/sorted list
    Returns True if the element is found and False otherwise"""

    # Start the search at position/index 0
    pos = 0
    # Target becomes true if the ele is in the list
    found = False
    stopped = False

    # Iterate until the end of the list
    while pos < len(arr) and not found and not stopped:
        
        # If matched retrun True
        if arr[pos] == ele:
            found = True
        # Else move to the next element
        else:

            if arr[pos] > ele:
                stopped = True
            else:
                pos += 1

    return found

arr = [1, 2, 3, 5, 6, 7]
print(orederd_seq_search(arr, 10))
