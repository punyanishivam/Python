# YodaJedi
import math


def no_of_jedi(arr, yoda, jedi):

    count = 10000
    jedi_count = 0
    index = 0

    for i in range(len(arr)):
        if arr[i] < yoda:
            continue
        value = arr[i] - yoda
        jedi_count = math.ceil(value / jedi)
        if jedi_count < count:
            count = jedi_count
            # print(count)
            index = i
            print(index)

    for i in range(len(arr)):
        if i != index:
            jedi_count = math.ceil(arr[i] / jedi)
            count += jedi_count

    return count


arr = [4, 7, 10, 5, 6, 55]
yoda = 20
jedi = 3

print(no_of_jedi(arr, yoda, jedi))
