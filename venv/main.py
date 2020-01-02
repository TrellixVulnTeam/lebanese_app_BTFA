"""program for translating arabic characters into roman arabic script"""

#importing pydub for audio
from pydub import AudioSegment
from pydub.playback import play

#importing lebanese module stuff
from lebanese import breakdown_lebanese
from breakdown_lebanese import arabic_break_down
from lebanese import lebanese_to_roman
from lebanese_to_roman import arabic_to_roman_replace

#importing kivy stuff
import kivy
kivy.require('1.11.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class Translator(GridLayout):

    def __init__(self, **kwargs):
        super(Translator, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Input arabic word here to have it converted: "))
        self.test = TextInput(password=False, multiline=True,)
        self.add_widget(self.test)
# https://kivy.org/doc/stable/guide/basic.html#create-an-application
class MyApp(App):

    def build(self):
        return Translator()

"""    layout = BoxLayout(padding=10)
    button = Button(text='My first button')
    layout.add_widget(button)"""

if __name__ == '__main__':
    MyApp().run()


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