# Sum of XOR of all pairs in an array

def sum_xor(arr):
	
	result = 0

	for i in arr:
		result ^= (2 * i)

	return result


print(sum_xor([7, 3, 5]))