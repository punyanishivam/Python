# IsUnique
inputStr = "akfbuyel"
flag = True
inputStr = sorted(inputStr)
for i in range(len(inputStr) - 1):
    if inputStr[i] == inputStr[i+1]:
        flag = False
print(flag)