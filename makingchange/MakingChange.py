## This algorithm calculates the minimum number of coins required to make change

def make_change(n, coins):
    opt,largest = [-1]*(n+1),[-1]*(n+1)
    for j in range(n+1):
        opt[j] = float('inf')
        for i in range(len(coins)-1,-1,-1):
            if coins[i] == j:
                opt[j] = 1
                largest[j] = coins[i]
            elif coins[i] < j:
                a = 1 + opt[j-coins[i]]
                if a < opt[j]:
                    opt[j] = a
                    largest[j] = coins[i]

    coins_needed = opt[n]
    C = []
    while n > 0:
        C.append(largest[n])
        n -= largest[n]

    return coins_needed,C

