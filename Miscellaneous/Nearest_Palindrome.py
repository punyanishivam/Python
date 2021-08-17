# Nearest Palindrome
n = 123

# n = str(n)
# if n == n[::-1]:
#     print(n)
# n = int(n)

for i in range(1, 50):
    after   = str(n + i)
    before  = str(n - i)
    if after == after[::-1]:
        print(after)
        break
    if before  == before[::-1]:
        print(before)
        break