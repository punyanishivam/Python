def digit_power_sum(n):

	sum = 0
	n = str(n)
	
	for i in range(len(n)):
		print(i+1)
		print(int(n[i]))
		sum += int(n[i]) ** (i+1)

	return sum

print(digit_power_sum(89))