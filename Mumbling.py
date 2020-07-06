def accum(s):

    result = ""
    
    for i in range(len(s)):
        result += s[i].upper() + (i * s[i].lower())
        
    return result

s = "ZpglnRxqenU"
print(accum(s))