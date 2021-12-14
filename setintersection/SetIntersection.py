# This algorithm calculates the intersect of two set

def intersect_brute(set1, set2):
    intersect = []
    for item1 in set1:
        for item2 in set2:
            if item1 == item2:
                intersect.append(item1)
    return intersect


# This algorithm is bad, O(n^2)

# This algorithm calculates the intersect of two set
from searching import SearchingAlgorithms
from sorting import SortingAlgorithms


def intersect_binary_search(set1, set2):
    intersect = []
    SortingAlgorithms.insertion_sort(set1)
    for item in set2:
        if SearchingAlgorithms.binary_search(set1, 0, len(set1), item) != -1:
            intersect.append(item)
    return intersect

# This algorithm is bound by searching, therefore O(n lg n)