#from my.kv import arabic_input.text
def arabic_break_down(testWord):

    test_word_length = len(testWord)

    letter_pos = test_word_length
    arabic_char_print = ""
    for letter in testWord:
        letter_pos_string = " |" + str(letter_pos) + "| "
        #print(letter_pos_string, letter, end=" ")
        arabic_char_print += letter + " " + letter_pos_string
        letter_pos -= 1

    return arabic_char_print
    #return print(arabic_char_print, end=" ")
    #return print(arabic_char_print, end = " ")
