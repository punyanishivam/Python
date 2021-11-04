from collections import Counter


def delete_nth(order, max_e):

    order_dict = Counter(order)

    dicty = {}

    print(order_dict)

    for key, value in order_dict.items():
        if value > max_e:
            dicty.update({key: max_e})
        else:
            dicty.update({key: value})

    print(dicty)

    result = []

    for key, value in dicty.items():
        result += [key] * value

    return result


print(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3))
