def two_sum(arr, k):

	arr_dict = {}
	count = 0

	for i in arr:
		val = k - i
		if val in arr_dict:
			count += 1
		else:
			arr_dict[i] = k - i

	return count

arr = [3, 5, 2, -4, 8, 11]
k = 7

print(two_sum(arr, k))
