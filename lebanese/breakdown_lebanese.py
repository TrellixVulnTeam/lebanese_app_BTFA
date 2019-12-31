def arabic_break_down(testWord):
    letter_pos = 1
    arabic_char_print = ""
    for letter in testWord:
        letter_pos_string = " |" + str(letter_pos) + "| "
        #print(letter_pos_string, letter, end=" ")
        arabic_char_print += letter_pos_string + " " + letter
        letter_pos += 1
    return print(arabic_char_print, end=" ")
    #return print(arabic_char_print, end = " ")
