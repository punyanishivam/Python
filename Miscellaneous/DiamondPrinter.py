def diamond_printer(m):
    
    k = 0
    n = ord(m) - ord("A") + 1
    
    # Print upper triangle
    for i in range(1, n + 1):
        char = chr(ord("A") + i - 1)
        for j in range(1, n - i + 1):
            print(" "),
        while (k != (2 * i - 1)) :
            if (k == 0 or k == 2 * i - 2):
                print(char),
            else:
                print(" "),
            k += 1
        k = 0
        print("")
      
    n -= 1
  
    # Print lower triangle
    for i in range (n, 0, -1):
        char = chr(ord("A") + i - 1)
        for j in range(0, n-i+1) :
            print(" "),
        k = 0
        while (k != (2 * i - 1)) :
            if (k == 0 or k == 2 * i - 2) :
                print(char),
            else :
                print(" "),
            k = k + 1
        print("")
        
m = "F"
diamond_printer(m)