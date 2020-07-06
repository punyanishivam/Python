def repeatedString(s, n):
    
    if s == "a":
        return n

    a_count = s.count("a")

    i = 0
    while len(s) != n:
        s += s[i]
        if s[i] == "a":
            a_count += 1
        i += 1
        if i == len(s) - 1:
            i = 0

    return a_count

s = "aba"
n = 10

print(repeatedString(s, n))