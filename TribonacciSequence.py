def tribonacci(signature, n):

    result = []
    result.append(signature[0])
    result.append(signature[1])
    result.append(signature[2])

    first = signature[0]
    second = signature[1]
    third = signature[2]

    for i in range(n - 3):
    	value = first + second + third
    	result.append(value)
    	first = second
    	second = third
    	third = value
    
    return result

signature = [1, 1, 1]
n = 10
print(tribonacci(signature, n))