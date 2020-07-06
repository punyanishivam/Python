def longest_consec(strarr, k):
    
    max = 0
    result = ""
    
    for i in range(len(strarr)):
        temp = "".join(strarr[i:i+k])
        if len(temp) > max:
            max = len(result)
            result = temp
            
    return result


print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))