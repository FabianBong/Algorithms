# This algorithm will figure out if all elements in an array are distinct
from sorting import SortingAlgorithms


def elements_distinct_brute(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                return False
    return True

# This is bad, it requires O(n^2)


# This algorithm will figure out if all elements in an array are distinct

def elements_distinct_sorting(arr):

    SortingAlgorithms.insertion_sort(arr);

    for i in range(1,len(arr)):
        if arr[i] == arr[i-1]:
            return False
    return True

# This is better, requires O(n lg n) - bounded by sorting