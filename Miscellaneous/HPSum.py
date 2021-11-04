def series_sum(n):
    sum = 0

    for i in range(1, n+1):
        sum += 1 / (1 + ((i - 1) * 3))
    return str(round(sum, 3))


print(series_sum(3))
