from collections import Counter


def duplicate_encode(word):

    result = ""
    dicty = Counter(word.lower())

    for i in word.lower():
        if dicty.get(i) == 1:
            result += "("
        else:
            result += ")"

    return result


word = "mnIdkwen@(n@IbIIcmcP!!bPQe!a!FuFvH OGuu"
print(duplicate_encode(word))

")))((()))())))))))))))))())())))((((())"
")))((()))()))))))))))))))))())))()())))"
