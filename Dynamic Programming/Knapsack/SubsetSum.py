def subset_sum(W, wt):

    n = len(wt)

    t = [[False for i in range(W+1)] for i in range(n+1)]

    for i in range(n+1):
        t[i][0] = True

    for i in range(1, W+1):
        t[0][i] = False

    for i in range(1, n+1):
        for j in range(1, W+1):
            if j < wt[i-1]:
                t[i][j] = t[i-1][j]
            else:
                t[i][j] = (t[i-1][j] or t[i-1][j-wt[i-1]])

    return t[n][W]


print(subset_sum(9, [3, 34, 4, 12, 5, 2]))
