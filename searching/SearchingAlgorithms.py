## This is a simple binary search algorithm

def binary_search(arr, l, u, x):
    if l > u:
        return -1

    m = (l + u) //2

    if arr[m] == x:
        return m
    elif arr[m] > x:
        return binary_search(arr, l,m-1,x)
    else:
        return binary_search(arr, m+1, u, x)


# Time complexity is O(lg n)
