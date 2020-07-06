# Hungry Fish
inputList = [50, 25, 20, 9, 100]

moves = 0

while len(inputList) > 1:
    if inputList[0] > inputList[1]:
        inputList[1] += inputList[0]
        inputList.pop(0)
    else:
        if inputList[1] > 2 * inputList[0]:
            inputList.remove(1)
        else:
            inputList.insert(1, inputList[0] - 1)
            moves += 1
    
print(moves)