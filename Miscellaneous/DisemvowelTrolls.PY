def disemvowel(string):

    vowels = ['a', 'e', 'i', 'o', 'u']

    for i in vowels:
        string = string.replace(i, "")

    return string


string = "This website is for losers LOL"
print(disemvowel(string))
