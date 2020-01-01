from dictionaries import *

def arabic_to_roman_replace(test_word):
    """program for translating arabic characters into roman arabic script"""
    arabic_word = test_word

    dictionary_vowels = {
        "َ": "a",
        "ً": "////",
        "ُ": "u",
        "ٌ": "////",
        "ٍ": "////",
        "ِ": "i",
        "ْ": "////",
    }

    """
    testWord = "دَرْس"
    print(testWord, sep=" ")
    """

    # converting into roman characters
    print()
    roman_characters = ""
    for letter in arabic_word:
        print(letter, "test")
        if letter in Dictionary.set_lebanese_dictionary():
            roman_characters += Dictionary.get_lebanese_to_roman_char(letter) #.roman_text #Dictionary.get_lebanese_to_roman_char(letter)
        elif letter in dictionary_vowels:
            roman_characters += dictionary_vowels[letter]
            # print("test")
        elif letter == " ":
            roman_characters += " "
    print(str(roman_characters), str(test_word))

    # مِلْء
    #####plans for improving the program#####
    """so it seems I need to add a condition for certain letters being first followed by letters and certain letters being sandwiched by other words
    for example in صباح الخير the program thinks this is sbah alkhyr when it should be sabah alkhair
    add a condition for y letters wrapped by others to turn them into ai sound. also make a condition for s followed by another
    letter to add the sa instead of s"""
    # so we can take the current string in english and then translate this into another variable string that loops through the string and checks to see
    # if any certain letters are present relative to others and then from that outputs a new string with the correct spelling.

    # it would also be cool to have a command that asks if you would like to see the sound breakdown and provides wording like S(Sauce)abah alkyhair ect for each letter
    # or better yet use audio files of a voice to string together words.

    knownFirstLetterSoundShifts = {"ص":"sa",
                                   "ب":"bi",
                                   "ك": "ki"}
    """this part of the code is for converting the individual words down into its parts maybe make a seperate function with this and then use
    this new function for split_words and returning the new testWordSentence which will be used to convert arabic into roman characters? we should
    keep a copy like this though becuase the م ع <-- مع   and     ا ل س ل ا م ة <-- السلامة format is really good to look at"""
    split_words = test_word.split(" ")
    for word in range(len(split_words)):
        current_word = split_words[word]
        #print(current_word)
        for letter in range(len(current_word)):
            print(current_word[letter], end=" ")
            if letter == len(current_word)-1:
                print(end="<-- ")
            #if word == 0 and letter == 0 and
        print(current_word)

#same as above but it will return a new roman string thats completed
    split_words = test_word.split(" ")
    new_roman_string = ""
    for word in range(len(split_words)):
        current_word = split_words[word]
        for letter in range(len(current_word)):
            if current_word[letter] in dictionary:
                new_roman_string += dictionary[current_word[letter]]
            elif current_word[letter] in dictionary_vowels:
                new_roman_string += dictionary_vowels[current_word[letter]]
            elif current_word[letter] == len(current_word)-1:
                new_roman_string += " "
           ###replace these with a dictionary for punctuaton in arabic
            elif current_word[letter] == "؟": #some kind of question mark used in arabic instead of ? since arabic is backwards.
                new_roman_string += "?"
            elif current_word[letter] == ",":
                new_roman_string += ","
            else:
                new_roman_string += "\n--ERROR: ARABIC LETTER MISSING FROM A DICTIONARY" + f" --> missing letter: ( {current_word[letter]} ) --\n"
