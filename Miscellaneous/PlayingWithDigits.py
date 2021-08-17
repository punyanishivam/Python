def dig_pow(n, p):

    n = list(map(int, str(n)))
    
    result = 0
    
    for i in range(len(n)):
        result += n[i] ** (p + i)
        
    

n = 92
p = 1
print(dig_pow(n, p))