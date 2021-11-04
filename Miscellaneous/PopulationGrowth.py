def nb_year(p0, percent, aug, p):

    count = 0
    pop = 0

    while pop < p:
        pop = p0 + (p0 * (percent/100) + aug)
        count += 1
        p0 = pop

    return count


print(nb_year(1500, 5, 100, 5000))
