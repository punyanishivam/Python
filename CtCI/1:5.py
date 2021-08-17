#OneAway
def oneAway(str1, str2):
    #OneAwayCheck
    return abs(len(str1) - len(str2)) <= 1
    if len(str1) > len(str2):
        big = str1
        small = str2
    else:
        big = str2
        small = str1
    index1 = 0
    index2 = 0
    flag = False
    while(index2 < len(big) and index1 < len(small)):
        if (big[index1] != small[index2]):
            if flag:
                return False
            flag = True
            if len(big) == len(small):
                index1 += 1
        else:
            index1 += 1
        index2 += 1
    return True
        


#OneAwayTester
str1 = "pale"
str2 = "pdfe"
result = oneAway(str1, str2)
print(result)