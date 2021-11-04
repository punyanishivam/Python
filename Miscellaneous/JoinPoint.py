def sum_of_digits(n):
    sum1 = 0
    while n > 0:
        sum1 += int(n % 10)
        n = int(n / 10)
    return sum1


def join_point(s1, s2):
    for _ in range(50):
        if s1 == s2:
            return s1
        s1 += sum_of_digits(s1)
        s2 += sum_of_digits(s2)
    return "NOOOOO"


print(join_point(57, 78))
