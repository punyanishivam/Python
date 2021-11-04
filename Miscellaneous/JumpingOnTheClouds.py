def jumpingOnClouds(c):

    result = []

    i = 0
    while i != len(c):

        if c[i+2] == 0:
            result.append(i+2)
            i += 2
        elif c[i+1] == 0:
            result.append(i+1)
            i += 1

    return len(result)


c = [0, 0, 0, 1, 0, 0]

print(jumpingOnClouds(c))
