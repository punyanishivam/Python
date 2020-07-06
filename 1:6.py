#String compression
inputStr = "aabcccccaaa"
count = 1
result = ""
for i in range(len(inputStr) - 1):
    if inputStr[i] == inputStr[i+1]:
        count += 1
    else:
        result += inputStr[i] + str(count)
        count = 1
result += inputStr[-1] + str(count)
print(result)