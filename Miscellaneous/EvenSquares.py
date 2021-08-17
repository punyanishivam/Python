even_squares1 = [x*x for x in range(100) if x % 2 == 0]
print(even_squares1)

even_squares = []

for i in range(100):
	if i % 2 == 0:
		even_squares.append(i * i)

print(even_squares)

print(even_squares1 == even_squares)