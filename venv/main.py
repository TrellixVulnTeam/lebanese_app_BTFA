"""program for translating arabic characters into roman arabic script"""

import os

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
#from kivy.config import Config
#Config.set('modules', 'screen', 'phone_samsung_galaxy_s5')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.properties import ObjectProperty, NumericProperty, StringProperty

import kivy

kivy.require('1.11.1')  # replace with your current kivy version !
# from kivy.config import Config
# Config.set('modules', 'screen', 'phone_samsung_galaxy_s5')
from kivy.app import App

class TranslatorWidget(Widget):
    lebanese_arabic_text_input = ObjectProperty()

    #test_word = StringProperty("")
    #value = StringProperty("")

class MyApp(App):
    pass
   # def build(self):
     #   return TranslatorWidget()

if __name__ == '__main__':
    MyApp().run()

















class RootWidget(BoxLayout):
    pass

class Background(Widget):
    pass

class TranslatorLayout(FloatLayout):

    def __init__(self, **kwargs):
        super(TranslatorLayout, self).__init__(**kwargs)

        with self.image:
            Image(source="C:/Users/natha/PycharmProjects/translator/venv/images/background.png", allow_stretch = True,
                  pos=self.pos, size=self.size)
        #with self.canvas:
         #   Rectangle(source='C:/Users/natha/PycharmProjects/translator/venv/images/background.png', pos=self.pos, size=self.size)

        #self.cols = 2
        #self.add_widget(Label(text="Input arabic word here to have it converted: "))
        #self.test = TextInput(password=False, multiline=True,)
        #self.add_widget(self.test)

      #  "C:/Users/natha/PycharmProjects/translator/venv/images"

# https://kivy.org/doc/stable/guide/basic.html#create-an-application
class MyApp(App):

    def build(self):

        root = RootWidget()
        t = TranslatorLayout()
        root.add_widget(t)
        #root.add_widget(AsyncImage(
         #       source="C:/Users/natha/PycharmProjects/translator/venv/images/background.png",
           #     size_hint= (1, .5),
          #      pos_hint={'center_x':.5, 'center_y':.5}))

        #root.add_widget(t)
        return root
        #root.add_widget(AsyncImage("C:/Users/natha/PycharmProjects/translator/venv/images") )
        

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