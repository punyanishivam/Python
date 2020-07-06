def count_bits(n):
	rem = []
	while n > 2:
		rem.append(n % 2)
		n //= 2
	if n >= 2:
		rem.append(n // 2)
	else:
		rem.append(n)

	return rem[::-1].count(1)

print(count_bits(7))
