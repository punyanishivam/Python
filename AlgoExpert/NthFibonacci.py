def nth_fib(n):
	if n <= 1:
		return n
	else:
		return nth_fib(n-1) + nth_fib(n-2)

print(nth_fib(6))