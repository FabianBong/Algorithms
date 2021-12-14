## This algorithm is used to find the element with the maximum counts
from random import randint


def random_algo(arr):
    while True:
        i = randint(0, len(arr))
        count = arr.count(arr[i])
        if count > len(arr) / 2:
            return arr[i]


## Another algorithm always solves in O(n)
def fast_majority(arr):
    candidate = None
    counter = 0
    for item in arr:
        if counter == 0:
            candidate = item
            counter += 1
        elif item == candidate:
            counter += 1
        else:
            counter -= 1
    print(candidate)
