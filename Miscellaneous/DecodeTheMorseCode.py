def decodeMorse(morse_code):

    words = morse_code.split("   ")
    morse_code = [] * 100
    print(morse_code)
#     i = 0

#     for word in words:
#           morse_code[i].append(word.split(" "))
#           i += 1

    print(morse_code)


print(decodeMorse('.... . -.--   .--- ..- -.. .'))
