def funWithAnagrams(text):
    from collections import Counter
    i = 0
    text = sorted(text)
    while i < len(text) - 1:
        if Counter(text[i]) == Counter(text[i+1]):
                text.remove(text[i+1])
                i = 0
        else:
            i += 1
        

    return sorted(text)


text = ['code', 'aaagmnrs', 'anagrams', 'doce']
print(funWithAnagrams(text))
