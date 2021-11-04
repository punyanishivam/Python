def k_occurences(string, k):

    chardict = {}
    result = ""

    for i in string:
        if chardict.get(i):
            value = chardict.get(i)
            if value < k:
                chardict.update({i: value + 1})
                result += i
        else:
            chardict.update({i: 1})
            result += i

    return result


k = 2
string = "ababbca"
print(k_occurences(string, k))
