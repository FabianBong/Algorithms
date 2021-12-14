## This algorithm is trying to find three collinear points in a set of points
from elementdistinctness import ElementDistinctness
from sorting import SortingAlgorithms


def brute_force(set1):
    slope = lambda x1,y1,x2,y2: (y2 - y1) / (x2 - x1)
    for i in range(len(set1)):
        for j in range(i + 1, len(set1)):
            slope1 = slope(set1[i][0], set1[i][1], set1[j][0], set1[j][1])
            for k in range(j + 1, len(set1)):
                slope2 = slope(set1[i][0],set1[i][1], set1[k][0], set1[k][1])
                if slope1 == slope2:
                    return True
    return False

## We are trying every possibility. Therefore, O(n^3)

def sorting_distinctneses(set1):
    slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
    slope_list = []
    for i in range(len(set1)):
        for j in range(i+1,len(set1)):
            slope_list.append(slope(set1[i][0], set1[i][1], set1[j][0], set1[j][1]))

    SortingAlgorithms.insertion_sort(slope_list)

    return not ElementDistinctness.elements_distinct_sorting(slope_list)
