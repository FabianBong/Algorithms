# This algorithm finds the (continuous) subarray with the maximum sum

def brute_force(arr):
    max_sum = 0
    for l in range(len(arr)):
        for u in range(l, len(arr)):
            new_sum = 0
            for i in range(l, u):
                new_sum += arr[i]
                if new_sum > max_sum:
                    max_sum = new_sum
    return max_sum

# This algorithm is BAD, run time is O(n^3)

# This algorithm finds the (continuous) subarray with the maximum sum

def brute_force_prefix(arr):
    max_sum = 0
    for l in range(len(arr)):
        new_sum = 0
        for u in range(l,len(arr)):
            new_sum += arr[u]
            if new_sum > max_sum:
                max_sum = new_sum
    return max_sum

# This algorithm is better than bruteforce but still the run time is O(n^2)


# This algorithm finds the (continuous) subarray with the maximum sum
import math

def divide_and_conquer(arr,l,u):
    if l > u:
        return 0
    if l == u:
        return max(0,arr[l])

    m = math.floor((l+u)/2)

    sum_low = 0
    max_low = 0
    for i in range(m,l-1,-1):
        sum_low += arr[i]
        max_low = max(max_low, sum_low)

    sum_up = 0
    max_up = 0
    for i in range(m+1,u+1):
        sum_up += arr[i]
        max_up = max(max_up, sum_up)

    max_a = divide_and_conquer(arr, l,m)
    max_b = divide_and_conquer(arr, m+1, u)

    return max(max_a,max_b, max_up+max_low)


# This algorithm is way better, run time is O(n lg n)

# This algorithm finds the (continuous) subarray with the maximum sum

def linear_scan(arr):
    max_so_far = 0
    max_suffix_sum = 0

    for i in range(len(arr)):
        max_suffix_sum = max(max_suffix_sum + arr[i], 0)
        max_so_far = max(max_so_far, max_suffix_sum)

    return max_so_far


# This algorithm is the best way, it only takes O(n)

# This algorithm finds the (continuous) subarray with the maximum sum

def prefix_sum(arr):
    P = [0] * len(arr)
    for i in range(len(arr)):
        P[i] = P[i-1] + arr[i]

    max_sum = 0
    for l in range(len(arr)):
        for u in range(l, len(arr)):
            new_sum = P[u] - P[l-1]
            if new_sum > max_sum:
                max_sum = new_sum
    return max_sum

# This algorithm is better, but still O(n^2)
