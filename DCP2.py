# What if we can't use division?
inputList = [1, 2, 3, 4, 5]
inputList2 = [3, 2, 1]
prod = 1
for i in inputList:
    prod *= i
outputList = [prod] * len(inputList)
for i in range(len(outputList)):
    outputList[i] = outputList[i] / inputList[i]
print(outputList)