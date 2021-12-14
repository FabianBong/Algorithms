## Most straight forward idea would be brute force. This, however, would be expontential

## However, we can use dynamic programming to come up with an elegant solution

def LCS_dynamic(str1,str2):
    c = [[-1] * (len(str2)+1) for i in range(len(str1)+1)]
    for i in range(len(str1)+1):
        c[i][0] = 0

    for i in range(len(str2)+1):
        c[0][i] = 0

    for i in range(1,len(str1)+1):
        for j in range(1,len(str2) + 1):
            if str1[i-1] == str2[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])

    return c[len(str1)][len(str2)]

