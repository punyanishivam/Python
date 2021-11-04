def equilibrium_index(arr):

    leftSum = 0
    totalSum = sum(arr)

    for i in range(len(arr)):
        totalSum -= arr[i]
        if leftSum == totalSum:
            return i
        leftSum += arr[i]

    return -1


arr = [3, -4, 2, -1, -3, 2, 1]
print(equilibrium_index(arr))
