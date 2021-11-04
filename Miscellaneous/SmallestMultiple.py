import fractions


def smallest_multiple(start, end):

    result = 1
    for i in range(start, end+1):
        result = (result*i) / fractions.gcd(result, i)
    return result


print(smallest_multiple(1, 10))
