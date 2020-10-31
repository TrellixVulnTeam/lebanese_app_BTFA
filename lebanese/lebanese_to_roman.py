from dictionaries import *

def arabic_to_roman_replace(test_word):
    """program for translating arabic characters into roman arabic script"""
    arabic_word = test_word

    """
    testWord = "دَرْس"
    print(testWord, sep=" ")
    """

    # converting into roman characters
    print()
    roman_characters = ""
    for letter in arabic_word:
        #print(letter)
        if letter in dictionary:
            roman_characters += Dictionary.get_lebanese_to_roman_char(letter) #.roman_text #Dictionary.get_lebanese_to_roman_char(letter)
        elif letter in dictionary_vowels:
            roman_characters += dictionary_vowels[letter]
            # print("test")
        elif letter == " ":
            roman_characters += " "
    return roman_characters
    ####print(str(roman_characters), str(test_word))

    # مِلْء
    #####plans for improving the program#####

#so it seems I need to add a condition for certain letters being first followed by letters and certain letters being sandwiched by other words
#for example in صباح الخير the program thinks this is sbah alkhyr when it should be sabah alkhair
#add a condition for y letters wrapped by others to turn them into ai sound. also make a condition for s followed by another
#letter to add the sa instead of s

# so we can take the current string in english and then translate this into another variable string that loops through the string and checks to see
# if any certain letters are present relative to others and then from that outputs a new string with the correct spelling.
# it would also be cool to have a command that asks if you would like to see the sound breakdown and provides wording like S(Sauce)abah alkyhair ect for each letter
# or better yet use audio files of a voice to string together words.

def get_word_breakdown(testword):
    test_word = testword

#this part of the code is for converting the individual words down into its parts maybe make a seperate function with this and then use
 #   this new function for split_words and returning the new testWordSentence which will be used to convert arabic into roman characters? we should
  #  keep a copy like this though becuase the م ع <-- مع   and     ا ل س ل ا م ة <-- السلامة format is really good to look at

    split_words = test_word.split(" ")
    split_words.reverse()
    word_breakdown = ""
    for word in range(len(split_words)):
        current_word = split_words[word]
        #print(current_word)
        for letter in range(len(current_word)):
            word_breakdown += current_word[letter] + " "
            #print(current_word[letter], end=" ")
            if letter == len(current_word)-1:
                word_breakdown += "<--"
                #print(end="<-- ")
            #if word == 0 and letter == 0 and
        if current_word == split_words[len(split_words)-1]:
            word_breakdown += current_word
        else:
            word_breakdown += current_word + "\n"

    return(word_breakdown)

def get_new_roman_string(testword):
    test_word = testword
#same as above but it will return a new roman string thats completed
    split_words = test_word.split(" ")
    new_roman_string = ""
    for word in range(len(split_words)):
        current_word = split_words[word]
        current_word = current_word[::-1]
        for letter in range(len(current_word)):
            #print(letter)

            #I might have to use "unicodedata" module to check if the letter is in dictionary.

            #THE BUG IS THAT I DIDN'T ACCOUNT FOR FRONT MIDDLE AND END TYPE CHARACTERS FOR EACH CHARACTERS
            #THATS WHY EVEN IF I ADD NEW STRINGS IN IT DOESN'T UNDERSTAND ALL THE FORMS!
            #I NEED TO GET THE START WORDS MIDDLE WORDS AND END WORDS AS SEPERATE DICTIONARIES
            if current_word[letter] in dictionary_x:
                print(letter, current_word[letter])
                new_roman_string += dictionary_x[current_word[letter]]
          #  elif current_word[letter] in maybe:
           #     new_roman_string += current_word[letter] + "THIS IS IT"
            #elif current_word[letter] in big_dictionary:
             #   new_roman_string += "FOUND IN big_dictionary, This is probably an error that I need to fix"
            elif current_word[letter] in dictionary:
                new_roman_string += dictionary[current_word[letter]]
            elif current_word[letter] in dictionary_vowels:
                new_roman_string += dictionary_vowels[current_word[letter]]
            ###replace these with a dictionary for punctuaton in arabic
            elif current_word[letter] == "؟": #some kind of question mark used in arabic instead of ? since arabic is backwards.
                new_roman_string += "?"
            elif current_word[letter] == ",":
                new_roman_string += ","
            else:
                new_roman_string += "\n--ERROR: ARABIC LETTER MISSING FROM A DICTIONARY" + f" --> missing letter: ( {current_word[letter]} ) --\n"
        new_roman_string += " "
    return new_roman_string