def main():
    i = 1
    while i < 10:
        j = 2
        while j <= (i / j):
            if not i % j == 0:
                break
            if (j > (i/j)) and i < (i+j):
                print(i+1)
        i += 1


print(main())
