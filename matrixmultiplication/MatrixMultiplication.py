## This algorithm finds the best way to multiply matrices


## This is a bad algorithm, it is similar to bruteforce and requires exponential time
# i = strart Matrix (from 1)
# j = end matrix
# p = dimensions p-1 and p is of M1 and so on and so forth
def matrix_multiplication_recursive(i,j,p):
    if i == j:
        return 0
    else:
        minc = float('inf')
        for k in range(i, j):
            a = matrix_multiplication_recursive(i,k,p)
            b = matrix_multiplication_recursive(k+1,j,p)
            minc = min(minc, a+b+p[i-1]*p[k]*p[j])
    return minc


## We have to fix the order which we calculate the options in
# n = number of matrices starting from 1
def matrix_multiplication_recursive_order(p,n):
    m = [[0]*(n+1) for i in range(n+1)]
    for i in range(n):
        m[i][i] = 0

    for d in range(1,n+1):
        for i in range(1,n-d+1):
            j = i+d
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q

    return m[1][n]



## We can also use memoization

# n = number of matrices starting from 1
def matrix_multiplication_memoized(p,n):
    m = [[0] * (n + 1) for i in range(n + 1)]
    for i in range(n+1):
        for j in range(n+1):
            m[i][j] = float('inf')

    return matrix_multiplication_memoized_helper(p,1,n,m)


def matrix_multiplication_memoized_helper(p,i,j,m):
    if m[i][j] < float('inf'):
        return m[i][j]

    if i == j:
        m[i][j] = 0

    else:
        for k in range(i,j):
            q = matrix_multiplication_memoized_helper(p,i,k,m) + matrix_multiplication_memoized_helper(p,k+1,j,m) + p[i-1]*p[k]*p[j]
            if q < m[i][j]:
                m[i][j] = q

    return m[i][j]