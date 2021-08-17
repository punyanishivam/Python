def LetterChanges(str1):
    result = ""
    final = ""
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for i in str1:
        if i.isalpha():
            if i == 'z':
                result += 'a'
            else:
                n = ord(i)
                n += 1
                n = chr(n)
                result += n
        else:
            result += i
    for i in result:
        if i in vowels:
            final += i.upper()
        else:
            final += i
      
    return final

# keep this function call here 
print(LetterChanges("hello*3"))