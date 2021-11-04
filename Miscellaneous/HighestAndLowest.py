def high_and_low(numbers):

    numbers = numbers.split(" ")

    num_list = []

    for i in numbers:
        num_list.append(int(i))

    print(max(num_list))
    return str(max(num_list)) + " " + str(min(num_list))


numbers = "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"
print(high_and_low(numbers))
