# Number of Pairs
def sockMerchant(n, ar):
    dict = {}
    pairs = 0

    for i in ar:
        if dict.get(i):
            value = dict.get(i)
            value += 1
            dict.update({i: value})
        else:
            dict.update({i: 1})

    for key, value in dict.items():
        if value > 1:
            pairs += value // 2

    return pairs


n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

print(sockMerchant(n, ar))
