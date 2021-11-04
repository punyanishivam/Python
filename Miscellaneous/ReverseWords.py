def spin_words(sentence):
    list1 = sentence.split(" ")
    for i in list1:
        value = len(i)
        if value % 2 != 0:
            rev = i[::-1]
            list1.append(rev)
        else:
            list1.append(i)
    return list1


sentence = "This is another test"

print(spin_words(sentence))
