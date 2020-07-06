# No_of_pairs

def no_of_pairs(arr):

	my_dict = {}
	count = 0

	for i in arr:
		l = []
		for j in str(i):
			if j != "0":
				l.append(int(j))

		my_dict.update({i : l})

	print(my_dict)

	for k1, v1 in my_dict.items():
		for k2, v2 in my_dict.items():
			if k1 != k2:
				if sorted(v1) == sorted(v2):
					count += 1

	return count//2




arr = [1024, 4021, 204, 303, 33, 603, 36, 55, 505]
print(no_of_pairs(arr))