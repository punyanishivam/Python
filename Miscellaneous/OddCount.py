# WAP to find the integer whose count is odd.


def odd_count(arr):
    dicty = {}

    for i in arr:
        if i in dicty.keys():
            val = dicty[i]
            val += 1
            dicty.update({i: val})
        else:
            dicty[i] = 1
    for i in dicty:
        if dicty[i] % 2 != 0:
            return i


arr = [2, 1, 1, 2, 2, 4, 5, 5, 2]
print(odd_count(arr))
