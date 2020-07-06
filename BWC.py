def main():

    n = 10
    team_g = [3, 6, 7, 5, 3, 5, 6, 2, 9, 1]
    team_a = [2, 7, 0, 9, 3, 6, 0, 6, 2, 6]
    count = 0

    for i in range(n):
        n = team_a[i]
        value = find_small(team_g, n)
        if value:
            count += 1
            team_g.remove(value)

    print(count)


def find_small(arr, n):

    min_element = max(arr)

    for i in arr:
        if i > n and i <= min_element:
            min_element = i
            return min_element

    return None


main()
