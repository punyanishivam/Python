# Given n, print all the numbers from 1 to n and n to 1 using recursion.


def print_asc(n):
    if n == 0:
        return
    else:
        print_asc(n-1)
        print(n)


def print_desc(n):
    if n == 0:
        return
    else:
        print(n)
        print_desc(n-1)


print_asc(10)
# print_desc(10)
