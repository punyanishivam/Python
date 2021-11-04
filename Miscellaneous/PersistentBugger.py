def persistence(n):

    if n < 10:
        return 0

    arr = list(map(int, str(n)))
    result = mul_of_digits(arr)

    while result > 10:
        result = list(map(int, str(result)))
        result = mul_of_digits(result)

    return result


def mul_of_digits(arr):

    result = 1

    for i in arr:
        result *= i

    return result


n = 999
print(persistence(n))
