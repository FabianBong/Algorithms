## This class is used to test each algorithm
import setintersection.SetIntersection
from collinearpoints import CollinearPoints
from convexhull import ConvexHull
from egyptianfractions import EgyptianFractions
from elementdistinctness import ElementDistinctness
from graphs import MinimumSpanningTree, SingleSourceShortestPath
from greatestcommondivisor import GreatestCommonDivisor
from longestcommonsubsequence import LongestCommonSubsequence
from majorityelement import MajorityElement
from makingchange import MakingChange
from matrixmultiplication import MatrixMultiplication
from maxsubrangesum import MaxSubRangeSum
from searching import SearchingAlgorithms
from setintersection import SetIntersection

arr1 = [31,-41,59,26,-53,58,97,-93,-23,84]
arr2 = [-41,59,26,58,97,-93,-23,84,54,2,5]
arr3 = [1,1,1,1,1,1,1,5,2,6,7,4,1,1,1,5,3,66]
points = [[0,5],[9,4],[7,3],[6,1],[10,10],[11,11],[12,12]]



## Insertion sort

# print(InsertionSort.insertion_sort(arr))

## Max Sub Array Sum
# print(MaxSubRangeSum.brute_force(arr1))
# print(MaxSubRangeSum.prefix_sum(arr1))
# print(MaxSubRangeSum.brute_force_prefix(arr1))
# print(MaxSubRangeSum.divide_and_conquer(arr1,0,len(arr1)-1))
# print(MaxSubRangeSum.linear_scan(arr1))

## Element distinctness
# print(ElementDistinctness.elements_distinct_brute(arr))
# print(ElementDistinctness.elements_distinct_sorting(arr))

## Binary search
# InsertionSort.insertion_sort(arr)
# print(SearchingAlgorithms.binary_search(arr, 0, 9,58))

## Set Intersection
# print(SetIntersection.intersect_brute(arr1,arr2))
# print(SetIntersection.intersect_binary_search(arr1,arr2))

## CollinearPoints
# print(CollinearPoints.brute_force(points))
# print(CollinearPoints.sorting_distinctneses(points))

## ConvexHull
# print(ConvexHull.jarvis_march(points))

## MinimumSpanningTree
# Kruskal
# V = 5
# parent = [i for i in range(V)]
# INF = float('inf')
# cost = [[INF, 2, INF, 6, INF],
#        [2, INF, 3, 8, 5],
#        [INF, 3, INF, INF, 7],
#        [6, 8, INF, INF, 9],
#        [INF, 5, 7, 9, INF]]
# MinimumSpanningTree.kruskals(cost,parent,V)

# Prims
# graph =[[0, 2, 0, 6, 0],
#        [2, 0, 3, 8, 5],
#        [0, 3, 0, 0, 7],
#        [6, 8, 0, 0, 9],
#        [0, 5, 7, 9, 0]]
# MinimumSpanningTree.prims(graph,V)

## Single Source Shortest Path
# print(SingleSourceShortestPath.bellman_ford(graph,V,0))
# print(SingleSourceShortestPath.dijkstra(graph,V,0))

## Majority Element
# print(MajorityElement.random_algo(arr3))
# print(MajorityElement.fast_majority(arr3))


## GCD
# print(GreatestCommonDivisor.brute_force(245,635))
# print(GreatestCommonDivisor.euclid(245,635))
# print(GreatestCommonDivisor.binary_gcd(245,635))

## Making change
# print(MakingChange.make_change(8,[1,4,5]))


## Longest Common Subsequence
# print(LongestCommonSubsequence.LCS_dynamic("algorithm","exploration"))

## Egyptian Fractions
# print(EgyptianFractions.egpytian_fraction(22,333))

## Matrix Multiplication
# print(MatrixMultiplication.matrix_multiplication_recursive(1,4,[5,6,9,3,10]))
# print(MatrixMultiplication.matrix_multiplication_recursive_order([5,6,9,3,10],4))
# print(MatrixMultiplication.matrix_multiplication_memoized([5,6,9,3,10],4))

