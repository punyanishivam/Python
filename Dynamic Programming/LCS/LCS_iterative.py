# Longest Common Sequence using Dynamic Programming

def lcs(X, Y):

    m = len(X)
    n = len(Y)
    
    t = [[0 for j in range(n+1)] for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                t[i][j] = 0
            elif (X[i-1] == Y[j-1]):
                t[i][j] = 1 + t[i-1][j-1]
            else :
                t[i][j] = max(t[i][j-1], t[i-1][j])

    return t[m][n]


X = "abppplee"
Y = "apple"
print("Length of LCS is ", lcs(X, Y))
