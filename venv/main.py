"""program for translating arabic characters into roman arabic script"""

from pydub import AudioSegment
from pydub.playback import play
from lebanese import breakdown_lebanese
from breakdown_lebanese import arabic_break_down
from lebanese import lebanese_to_roman
from lebanese_to_roman import arabic_to_roman_replace

#example arabic word دَرْس
def main():
    #sound = AudioSegment.from_file("C:/Users/natha/Desktop/house_lo.wav", format="wav")
    #play(sound)
    # inputting the word itself
    test_word = input("Input arabic word here to have it converted: ")
    print(test_word, sep=" ")
    breakdown_lebanese.arabic_break_down(test_word)
    lebanese_to_roman.arabic_to_roman_replace(test_word)
if __name__ == '__main__':
    main()