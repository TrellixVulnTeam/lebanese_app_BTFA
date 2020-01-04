
dictionary = {"ا": "a",
              "ب": "b",
              "ت": "t (tan)",
              "ث": "th (THin)",
              "ج": "j",
              "ح": "h",
              "خ": "kh",
              "د": "d",
              "ذ": "th",  # (THat)",
              "ر": "r",
              "ز": "z",
              "س": "s",
              "ش": "sh",
              "ص": "S",  # (Sauce / Sob)",
              "ض": "D (dawn)",
              "ط": "t (Taught)",
              "ظ": "th (Though)",
              "ع": "ah while constricting throat",
              "غ": "french r gargling",
              "ف": "f",
              "ق": "q",
              "ك": "k",
              "ل": "l",
              "م": "m",
              "ن": "n",
              "ه": "h",
              "و": "w",
              "ي": "y"}

dictionary_vowels = {"َ": "a",
                    "ً": "////",
                    "ُ": "u",
                    "ٌ": "////",
                    "ٍ": "////",
                    "ِ": "i",
                    "ْ": "////"}

known_first_letter_sound_shifts = {"ص": "sa",
                                   "ب":"bi",
                                   "ك": "ki"}

class Dictionary:
    def __init__(self):
        pass

    @staticmethod
    def get_lebanese_to_roman_char(letter):
        arabic_char = letter
        roman_text = dictionary[arabic_char]
        return roman_text