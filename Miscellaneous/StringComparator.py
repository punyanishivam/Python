from functools import cmp_to_key


def order(sentence):
    return sorted(sentence, key=cmp_to_key(compare))


def compare(x, y):

    a = ""
    b = ""

    for i in x:
        if i.isdigit():
            a += str(i)

    for i in y:
        if i.isdigit():
            b += str(i)

    if int(a) > int(b):
        return -1
    return 1


x = "pe6ople"
y = "th5ese"
print(compare(x, y))
